package main

import (
    "bytes"
    "image"
    "image/jpeg"
    "io"
    "net/http"
    "strconv"
    "io/ioutil"

    "github.com/anthonynsimon/bild/adjust"
    "github.com/anthonynsimon/bild/effect"
    "github.com/anthonynsimon/bild/transform"
    "github.com/anthonynsimon/bild/blur"
)

func homeHandler(w http.ResponseWriter, r *http.Request) {
    // Reading HTML file
    html, err := ioutil.ReadFile("dz.html")
    if err != nil {
        http.Error(w, "Unable to read index.html", http.StatusInternalServerError)
        return
    }

    // Sending HTML content
    w.Header().Set("Content-Type", "text/html")
    w.Write(html)
}

func main() {
    http.HandleFunc("/", homeHandler)
    http.HandleFunc("/upload", uploadHandler)
    http.ListenAndServe(":8080", nil)
}

func uploadHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method != "POST" {
        http.Redirect(w, r, "/", http.StatusSeeOther)
        return
    }

    r.ParseMultipartForm(10 << 20) // 10 MB
    file, _, err := r.FormFile("image")
    if err != nil {
        http.Error(w, "Error retrieving the file", http.StatusInternalServerError)
        return
    }
    defer file.Close()

    img, _, err := image.Decode(file)
    if err != nil {
        http.Error(w, "Error decoding the image", http.StatusInternalServerError)
        return
    }

    filter := r.FormValue("filter")
    rotation, _ := strconv.Atoi(r.FormValue("rotation"))
    brightness, _ := strconv.Atoi(r.FormValue("brightness"))
    blurAmount, _ := strconv.ParseFloat(r.FormValue("blur"), 64)

    // Apply selected filter
    switch filter {
    case "grayscale":
        img = effect.Grayscale(img)
    case "sepia":
        img = effect.Sepia(img)
    case "invert":
        img = effect.Invert(img)
    }

    // Apply additional features
    if rotation != 0 {
        img = transform.Rotate(img, float64(rotation), nil)
    }

    if brightness != 0 {
        img = adjust.Brightness(img, float64(brightness)/100.0)
    }

    if blurAmount > 0 {
        img = blur.Gaussian(img, blurAmount)
    }

    // Sending the processed image
    buffer := new(bytes.Buffer)
    if err := jpeg.Encode(buffer, img, nil); err != nil {
        http.Error(w, "Failed to encode image", http.StatusInternalServerError)
        return
    }

    w.Header().Set("Content-Type", "image/jpeg")
    io.Copy(w, buffer)
}
