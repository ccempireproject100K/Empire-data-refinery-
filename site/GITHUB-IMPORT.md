# Importing the 20/20 project into GitHub

The project is ready to import into a GitHub repository. The current managed checkpoint is `cc2747e`.

## Option A — GitHub website

1. Create a new repository on GitHub.
2. Download and unzip the editable project export.
3. In the repository, choose **Add file → Upload files**.
4. Upload the contents of the unzipped `20-20-data-refinery` folder, including `package.json`, `server.js`, `public/`, `scripts/`, `TODO.md`, and `plan.md`.
5. Commit the files to the repository’s default branch.

## Option B — Git command line

```bash
git init
git add .
git commit -m "Import 20/20 Data Refinery"
git branch -M main
git remote add origin https://github.com/YOUR-ACCOUNT/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the repository URL with the one created in your GitHub account. Do not commit `.env` files, API keys, or credentials.

## Run locally

```bash
npm start
```

Open `http://localhost:3000`.
