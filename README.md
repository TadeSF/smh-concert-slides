# Konzert Slides Template of Sommerliche Musiktage Hitzacker

### Get Started
To start the slide show:

- `npm install`
- `npm run dev`
- visit http://localhost:3030

### Edit Slides
Start editing the slides in the [pages](./pages) folder. In there – sorted by year – you find the respectiv slides for each concert.

If you edit the pages, you need to acknowledge a few things:
- Every slide needs to start with a `---` and end with a `---`. Every slide has a header and a body, which are once again separated by `---`. The header is used for the layout and the body for the content. In this context, the body can be left empty in almost all cases. The important step is to set the header to the right `layout` and its corresponding properties (see below). If needed, all other header configurations can be found in the [Slidev documentation](https://sli.dev/guide/syntax.html#slide-attributes).

There are a few layouts available:
- `banner` – a full screen image
- `piece` – a piece with composer, name, (subtitle), movements, columns and clicks
    - `composer` – the composer
    - `name` – the name of the piece
    - `subtitle` – the subtitle of the piece (optional)
    - `movements` – the movements of the piece
    - `columns` – the number of columns (change it so that the movements fit and look nicely arranged)
    - `clicks` – the number of movements plus one (this is for highlighting the movements in the correct order. If you dont want this option, just set it to 0 or leave it out)
- `song` – the same as piece, but with space for lyrics. Coming soon!
- `logo` – the logo of the festival

You can find an [example file](./pages/example.md) in the pages directory.

### Activate a concert
Activate a concert by changing the path inside [slides.md](./slides.md) to see the changes.

Learn more about Slidev on [documentations](https://sli.dev/).
