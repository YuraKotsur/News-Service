from django.db import models


# - Create CRUD API to manage news posts. The post will have the next fields: title, link, creation date, amount of upvotes, author-name
# - Posts should have CRUD API to manage comments on them. The comment will have the next fields: author-name, content, creation date
# - There should be an endpoint to upvote the post
# - We should have a recurring job running once a day to reset post upvotes count


class CategoryAbstract(models.Model):
    title                       = models.CharField(max_length=200, verbose_name='Title')

    def __str__(self):
        return self.title

class ArticleAbstract(models.Model):

    category                    = models.ForeignKey(CategoryAbstract, on_delete=models.CASCADE, verbose_name='Category' )
    title                       = models.CharField(max_length=250, verbose_name='Title')
    article_content             = models.TextField(verbose_name='Content')
    article_creation_date       = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    amount_of_votes             = models.IntegerField(default=0, verbose_name='Amount of votes')
    slug                        = models.SlugField(verbose_name='Slug')
    author_name                 = models.CharField(max_length=100, verbose_name='Author name')

    def __str__(self):
        return self.title


class CommentAbstract(models.Model):
    news                        = models.ForeignKey(ArticleAbstract, on_delete=models.CASCADE)
    author_name                 = models.CharField(max_length=100, verbose_name='Author name')
    comment_content             = models.TextField(verbose_name='Comment content')
    comment_creation_date       = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')

    def __str__(self):
        return self.author_name


class Comment(CommentAbstract):
    pass

class Category(CategoryAbstract):
    pass

class Article(ArticleAbstract):
    pass









