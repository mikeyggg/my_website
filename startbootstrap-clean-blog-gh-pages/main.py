from flask import Flask,render_template,request
from github_fetcher import get_projects
from email_sender import send_email
import random

app = Flask(__name__)

POSTS_PER_PAGE = 5
@app.route("/")
@app.route("/page/<int:page>")
def home(page=1):
    all_posts = get_projects()
    total_pages = -(-len(all_posts) // POSTS_PER_PAGE)

    if page > total_pages or page < 1:
        page = 1

    start = (page -1) *POSTS_PER_PAGE
    end = start + POSTS_PER_PAGE
    paginated_posts = all_posts[start:end]

    return render_template(
        "index.html",posts=paginated_posts,
        page=page,
        total_pages=total_pages,
    )

@app.route("/about-me")
def about():
    return render_template("about.html")

@app.route("/contact",methods=["GET","POST"])
def contact():

    if request.method == "GET":
        return render_template("contact.html")

    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        formated_message = (f"Hi im {name}\n"
                            f"{message}\n"
                            f"If you want to contact me my phone number is {phone} ")

        send_email(email,formated_message)
        return render_template("contact.html")


@app.route("/random-post")
def random_post():
    all_posts = get_projects()
    post = random.choice(all_posts)

    return render_template("post.html",
                           post_data =post)


@app.route("/post/<int:post_id>/<string:post_title>")
def blog(post_id,post_title):
    all_posts = get_projects()
    post = next((p for p in all_posts if p["id"] == post_id), None)

    if post is None:
        return "Post not found",404

    return render_template("post.html",
                           post_data = post)

if __name__ == "__main__":
    app.run(debug=True)