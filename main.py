from django.utils import timezone

from Django_blog_logika.django_blog_git import Post, Comment


def create_post(title, content):
    post = Post(title=title, content=content, publication_date=timezone.now())
    post.save()
    return post


def create_comment(post, text, author):
    comment = Comment(post=post, text=text, author=author, creation_date=timezone.now())
    comment.save()
    return comment


def get_posts():
    return Post.objects.all()


def get_comments_for_post(post):
    return post.comments.all()


def update_post(post, title=None, content=None):
    if title:
        post.title = title
    if content:
        post.content = content
    post.save()


def delete_post(post):
    post.delete()


def update_comment(comment, text=None):
    if text:
        comment.text = text
    comment.save()


def delete_comment(comment):
    comment.delete()


def print_posts():
    posts = get_posts()
    for p in posts:
        print(f'ID: {p.id}, Назва: {p.title}, Дата публікації: {p.publication_date}')


def print_comments(post):
    comments = get_comments_for_post(post)
    for c in comments:
        print(f'ID коментаря: {c.id}, Коментар: {c.text}, Автор: {c.author}, Дата створення: {c.creation_date}')


def main():
    while True:
        print("\nОберіть дію:")
        print("1. Додати пост")
        print("2. Додати коментар")
        print("3. Оновити пост")
        print("4. Видалити пост")
        print("5. Оновити коментар")
        print("6. Видалити коментар")
        print("7. Переглянути всі пости")
        print("8. Переглянути коментарі до посту")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            title = input("Введіть заголовок посту: ")
            content = input("Введіть зміст посту: ")
            create_post(title, content)
            print("Пост додано!")

        elif choice == "2":
            post_id = int(input("Введіть ID посту, до якого потрібно додати коментар: "))
            try:
                post = Post.objects.get(id=post_id)
                text = input("Введіть текст коментаря: ")
                author = input("Введіть автора коментаря: ")
                create_comment(post, text, author)
                print("Коментар додано!")
            except Post.DoesNotExist:
                print("Пост з таким ID не знайдено.")

        elif choice == "3":
            post_id = int(input("Введіть ID посту для оновлення: "))
            try:
                post = Post.objects.get(id=post_id)
                new_title = input("Введіть новий заголовок (залиште порожнім для без змін): ")
                new_content = input("Введіть новий зміст (залиште порожнім для без змін): ")
                update_post(post, title=new_title or None, content=new_content or None)
                print("Пост оновлено!")
            except Post.DoesNotExist:
                print("Пост з таким ID не знайдено.")

        elif choice == "4":
            post_id = int(input("Введіть ID посту для видалення: "))
            try:
                post = Post.objects.get(id=post_id)
                delete_post(post)
                print("Пост видалено!")
            except Post.DoesNotExist:
                print("Пост з таким ID не знайдено.")

        elif choice == "5":
            comment_id = int(input("Введіть ID коментаря для оновлення: "))
            try:
                comment = Comment.objects.get(id=comment_id)
                new_text = input("Введіть новий текст коментаря (залиште порожнім для без змін): ")
                update_comment(comment, text=new_text or None)
                print("Коментар оновлено!")
            except Comment.DoesNotExist:
                print("Коментар з таким ID не знайдено.")

        elif choice == "6":
            comment_id = int(input("Введіть ID коментаря для видалення: "))
            try:
                comment = Comment.objects.get(id=comment_id)
                delete_comment(comment)
                print("Коментар видалено!")
            except Comment.DoesNotExist:
                print("Коментар з таким ID не знайдено.")

        elif choice == "7":
            print_posts()

        elif choice == "8":
            post_id = int(input("Введіть ID посту для перегляду коментарів: "))
            try:
                post = Post.objects.get(id=post_id)
                print_comments(post)
            except Post.DoesNotExist:
                print("Пост з таким ID не знайдено.")

        elif choice == "0":
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()