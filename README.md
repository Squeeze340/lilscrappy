# lilscrappy

## Note

Found issue where the chrome dirver was outdated. Updated the local chromedriver version to 112 matching the chrome version of 112. Needed to add the new chrome driver binary to the `usr/local/bin` directory. Download link <https://chromedriver.storage.googleapis.com/index.html?path=112.0.5615.28/>

## Post structure

```

type Post struct {
	Heading     string
	MainContent string
	Author      Author
	Replys      []Reply
}

type Author struct {
	Name         string
	Link         string
	Level        int
	PostCount    int64
	HelpfulVotes int64
	Reviews      int64
}

type Reply struct {
	Date   string
	Content string
	Author Author
}
```