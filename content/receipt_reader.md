Title: Receipt Reader
Date: 2017-10-31
Category: Robots
Tags: computer vision, ocr, heroku
Slug: receipt_reader
Author: Brian Keating
Summary: Reading a receipt with OCR and parsing its contents.

I had the idea to write an app that reads and parses the contents of a photo of a receipt to allow for easy bill splitting. This idea came to me when splitting a large happy hour check with 15 friends. Personally, I don't care about the money, and after a few beers, I would happily pay more than my share, but some of the other people in our party were pretty anal -- breaking out the calculators, computing the tip down to the exact cent, etc. "There's got to be a better way!" I thought.  

Turns out [somebody alread had this idea](https://play.google.com/store/apps/details?id=com.bring10.tab&hl=en), but I thought this would be a good exercise, and that I might be able to write a more robust algorithm compared with the apps already on the market.


## Backend

I wound up writing the backend for a [receipt reader app](https://github.com/brikeats/receipt-reader). This is a flask app hosted on heroku. It accepts `GET` requests with a receipt image attached, and returns the parsed contents of the receipts as JSON. You can test it out by downloading [this image]({filename}/images/receipt.jpg) and sending it to the heroku server with with the command `curl -F "file=@receipt.jpg" https://receipt-reader-bk.herokuapp.com/` and, after a 15-second delay, the server should response with 

    {
      "items": [
        {
          "name": "Hac Cheese", 
          "price": 7.0, 
          "quantity": 1
        }, 
        {
          "name": "Madras Chicken Sando", 
          "price": 14.0, 
          "quantity": 1
        }, 
        {
          "name": "Mussels", 
          "price": 5.33, 
          "quantity": 1
        }, 
        {
          "name": "1/3 Charcuterie", 
          "price": 4.0, 
          "quantity": 1
        }, 
        {
          "name": "Brussel Sprouts", 
          "price": 2.0, 
          "quantity": 1
        }, 
        {
          "name": "Fries", 
          "price": 4.0, 
          "quantity": 1
        }, 
        {
          "name": "2 Half HA Tina", 
          "price": 10.0, 
          "quantity": 1
        }, 
        {
          "name": "Half SOB Goat", 
          "price": 5.0, 
          "quantity": 1
        }, 
        {
          "name": "Halt Beatbock", 
          "price": 4.0, 
          "quantity": 1
        }, 
        {
          "name": "Fun Lost Abbey", 
          "price": 6.0, 
          "quantity": 1
        }, 
        {
          "name": "Fun Wreckage", 
          "price": 7.0, 
          "quantity": 1
        }, 
        {
          "name": "Half A eman", 
          "price": 4.0, 
          "quantity": 1
        }, 
        {
          "name": "Full Whiner", 
          "price": 8.0, 
          "quantity": 1
        }
      ], 
      "subtotal": 80.33, 
      "total": 88.57
    }

Not quite perfect, but pretty damn good. I think it got all the prices right. Another example image is [here]({filename}/images/receipt2.jpg).


## Algorithm

### Preprocessing

The preprocessing script takes a possibly-shitty input image, and prepares it for OCR. Specifically,

* convert to grayscale
* median filter heavily
* use large-scale edge response to get the strongest:
    - horizontal line in the top half of the image
    - horizontal line in the bottom half of the image
    - vertical line in the left half of the image
    - vertical line in the right half of the image
   These lines are the receipt edges. This step assumes that the receipt is lighter in value than the background.
* Intersect the lines to get the corners of the receipt. 
* Warp so that the corners are axis-aligned. This makes the receipt image rectangular and has the effect of cropping out the background.

I initially experimented with directly detecting the corners using templates, rather than detecting the edges and then computing their intersection. I've found the method desribed above to be more robust to cast shadows that fall across the receipt and to work better when the receipt is not lying flat on the surface.

The notebook used to produce develop the preprocessing script can be viewed [here]({filename}/notebooks/preprocess.html) or downloaded [here]({filename}/notebooks/preprocess.ipynb).

### OCR

I used Azure's computer vision API to do the OCR. Google and amazon also offer such services, but Azure's API was the only one that returns the bounding box of each of the words. This is very important for parsing the contents. In addition to the word bounding boxes, the Azure API also tries to group the words into sections. I didn't find this to be useful at all.

### Parsing

All of the receipts that I've looked at for this project have the prices right-aligned with a small margin. The algorithm detects the prices first, and then reads the rest of the line:

* Select the words that have numerals
* Compute the coordinates of right-hand side (RHS) of all the numerical words
* Find a line that passes through a lot of the numerical word RHS's. This line should be close to vertical -- it is the right-hand margin of the receipt. The numerical words whose bounding boxes lie on the right-hand margin are probably prices.
* For each price-word, we get the other words whose bounding boxes have a similar y-location. These words are on the same line as the price-word, so they are the item names. 
* Parse the prices and convert to floating point. This should include fixing common OCR errors (like mixing up the letter "O" and the numeral zero).
* Search the item names for keywords "tax", "subtotal", and "total". This should include variants like "sub-total", "amount due", etc.

Finally the results are packed into a JSON object and served by Flask.

The notebook used to produce develop the OCR and content parsing can be viewed [here]({filename}/notebooks/azure_api.html) or downloaded [here]({filename}/notebooks/azure_api.ipynb).

## Front end

Although I've written [simple android apps](https://github.com/brikeats/Compass) for using my phone's sensors, I'm hardly an expert on Android development (I lean pretty hard on the IDE to help me out), so there's no functional frontend for this app. If you have Android development experience and are interested in building this out, send me an email!
