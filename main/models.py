from django.db import models

class Post(models.Model):
    '''данные о посте'''
    author = models.CharField('Имя автора', max_length=100)
    data = models.DateTimeField('Дата публикации')
    title = models.CharField('Заголовок записи', max_length=100)
    subtitle = models.CharField('Подзаголовок записи', max_length=300)
    img = models.ImageField('Изображение', upload_to='image/%Y')
    description = models.TextField('Текст записи')
    
    
    def __str__(self):
        return f'{self.title}, {self.author}'    
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        

class Comments(models.Model):
    '''Комменитарий'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комменитария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE )
    
    def __str__(self):
        return f'{self.name}, {self.post}'    
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'