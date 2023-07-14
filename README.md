# Konzert Slides Template of Sommerliche Musiktage Hitzacker

### Get Started
Clone this repository:
```bash
git clone https://github.com/TadeSF/smh-concert-slides
```


To start the slide show:
```bash
npm install
npm run dev
```
Then visit http://localhost:3030 (if it doesn't open automatically)

### Wrapper for the Slides
The concert slides are wrapped in a few other slides. These are:
- Video at the beginning
- Banner
- Mobile Warning (turn off devices notice)
- blank logo slide
- -> Content (the actual concert slides) <-
- blank logo slide
- Banner
- Video at the end

### Edit Slides
Start editing the slides in the [pages](./pages) folder. In there – sorted by year – you find the respectiv slides for each concert.

If you edit the pages, you need to acknowledge a few things:
- Every slide needs to start with a `---`. Every slide has a header and a body, which are once again separated by `---`. The header is used for the layout and the body for the content. In this context, the body can be left empty in almost all cases. The important step is to set the header to the right `layout` and its corresponding properties (see below). If needed, all other header configurations can be found in the [Slidev documentation](https://sli.dev/guide/syntax.html#slide-attributes).

There are a few layouts available:
- `banner` – a full screen image
- `logo` – the logo of the festival
- `piece` – a piece with composer, name, (subtitle), movements, columns and clicks
    - `composer` – the composer
    - `supertitle` – the supertitle (above the name) of the piece (optional)
    - `name` – the title of the piece ("title" is reserved for the title of the slide, hence we use "name" here)
    - `subtitle` – the subtitle of the piece (optional)
    - `movements` – the movements of the piece (in a list with `-` in front of each movement). Arrangement and click count are done automatically (optional)
    - `autoCountMovements` – boolean to turn on/off the automatic counting of movements (optional, default: `true`)
- `song` – the same as piece, but with space for lyrics. Coming soon!

You can find an [example file](./pages/example.md) in the pages directory.

### Activate a concert
Activate a concert by changing the path inside [slides.md](./slides.md) to see the changes.

Learn more about Slidev in their [documentation](https://sli.dev/).

### Utilities
The fastest way to add new concert slides is to use the custom vscode snippets provided by this repository. These are:
- `movements` – creates a piece with movements placeholder
- `nomovements` – creates a piece without movements placeholder (just composer and title)
- `logo` – creates a logo slide
- `banner` – creates a banner slide
- `break` – creates three slides:
  - blank logo slide
  - banner slide
  - blank logo slide