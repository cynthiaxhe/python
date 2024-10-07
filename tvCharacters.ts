import express, { Request, Response } from 'express';

const app = express();
const port = 3000;

const tvShows: { [key: string]: string[] } = {
  "Breaking Bad": ["Walter White", "Jesse Pinkman", "Skyler White", "Hank Schrader"],
  "Game of Thrones": ["Jon Snow", "Daenerys Targaryen", "Tyrion Lannister", "Arya Stark"],
  "Friends": ["Rachel Green", "Monica Geller", "Phoebe Buffay", "Joey Tribbiani", "Chandler Bing", "Ross Geller"]
};

app.get('/characters', (req: Request, res: Response) => {
  const showName = req.query.show as string;
  if (!showName) {
    return res.status(400).json({ error: "Please provide a TV show name" });
  }

  const characters = tvShows[showName];
  if (!characters) {
    return res.status(404).json({ error: "TV show not found" });
  }

  return res.json({ show: showName, characters });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});