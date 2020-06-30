# Digging up the past

## Challenge prompt
```
The photographer in this picture, and the one who took it, are both secret agents who work undercover for us in Russia. They managed to covertly send us this picture. We think it means something, or maybe something was hidden inside. Can you extract the information? It's a matter of national security!!
```
## **Solution**
```
This steganography challenge is quite simple.It can be solved in 2 ways.
```
- Low hanging fruit
    - ```strings photographer.jpg  | grep hackoff{.*}```

- Online version
    -``` Use any online tools to extract data from image```
- Extracting the data from the image
    - ```exiftool photographer.jpg | grep hackoff{.*}```

Both will give flag

## flag : hackoff{lots_0f_secrets_in_exiftags}



# ***Some info on Metadata***
```
We know that everything can be translated to data.These can be anything from the type of data to bytes inside the data object.

When we click a photograph we are just viewing the image.
- But what happens to the shutter speed used ? 
- Date and time of capture ?
- Dimensions of image ?
-etc ...


These are the data of the data or so called meta-data. Images have Exif data as meta-data. 
Exiftool is a linux tool to extract meta-data from images.
```