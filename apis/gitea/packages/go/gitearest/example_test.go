package gitearest_test

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log"
	"os"

	"github.com/fdhoff/api-sdks/apis/gitea/packages/go/gitearest"
)

// These examples are the README's, compiled so they stay current. They are not run.

func Example() {
	client, err := gitearest.NewClient("https://gitea.example.com", gitearest.Token(os.Getenv("GITEA_TOKEN")))
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	user, err := client.CurrentUser.Get(ctx)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*user.Login)

	params := &gitearest.IssuesListParams{State: gitearest.Ptr("open"), Limit: gitearest.Ptr[int64](50)}
	for issue, err := range client.Issues.Iter(ctx, "your-org", "your-repo", params) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*issue.Number, *issue.Title)
	}

	_, err = client.Repos.Get(ctx, "your-org", "missing-repo")
	var failure *gitearest.APIError
	if errors.Is(err, gitearest.ErrNotFound) && errors.As(err, &failure) {
		fmt.Println(failure.Status, failure.Detail)
	}
}

func Example_basic() {
	client, err := gitearest.NewClient(
		"https://gitea.example.com",
		gitearest.BasicWithOTP("your-username", os.Getenv("GITEA_PASSWORD"), "123456"),
	)
	if err != nil {
		log.Fatal(err)
	}
	token, err := client.Users.CreateToken(context.Background(), "your-username", &gitearest.CreateAccessTokenOption{
		Name:   gitearest.Ptr("scripts"),
		Scopes: []string{"read:repository"},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*token.SHA1)
}

func Example_sudo() {
	client, err := gitearest.NewClient(
		"https://example.com/git",
		gitearest.Token(os.Getenv("GITEA_ADMIN_TOKEN")),
		gitearest.WithSudo("another-user"),
	)
	if err != nil {
		log.Fatal(err)
	}
	for repo, err := range client.CurrentUser.IterRepos(context.Background(), &gitearest.CurrentUserListReposParams{Limit: gitearest.Ptr[int64](50)}) {
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(*repo.FullName)
	}
}

func Example_files() {
	client, err := gitearest.NewClient("https://gitea.example.com", gitearest.Token(os.Getenv("GITEA_TOKEN")))
	if err != nil {
		log.Fatal(err)
	}
	ctx := context.Background()

	file, err := client.Contents.DownloadRaw(ctx, "your-org", "your-repo", "docs/guide.md", &gitearest.ContentsDownloadRawParams{Ref: gitearest.Ptr("main")})
	if err != nil {
		log.Fatal(err)
	}
	defer file.Body.Close()
	if _, err := io.Copy(os.Stdout, file.Body); err != nil {
		log.Fatal(err)
	}

	attachment, err := client.Issues.UploadAttachment(ctx, "your-org", "your-repo", 1, &gitearest.IssuesUploadAttachmentParams{
		Name:       gitearest.Ptr("notes.txt"),
		Attachment: gitearest.File{Name: "notes.txt", Content: []byte("synthetic notes\n")},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(*attachment.BrowserDownloadURL)
}
