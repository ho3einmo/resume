from django.db import models

# Create your models here.
ICON_SKILL = [
    ('fab fa-python', 'Python'),
    ('fab fa-js', 'JavaScript'),
    ('fab fa-java', 'Java'),
    ('fab fa-node-js', 'Node.js'),
    ('fab fa-react', 'React'),
    ('fab fa-angular', 'Angular'),
    ('fab fa-vuejs', 'Vue.js'),
    ('fab fa-html5', 'HTML5'),
    ('fab fa-css3-alt', 'CSS3'),
    ('fab fa-git', 'Git'),
    ('fab fa-github', 'GitHub'),
    ('fab fa-docker', 'Docker'),
    ('fab fa-aws', 'AWS'),
    ('fab fa-linux', 'Linux'),
    ('fab fa-windows', 'Windows'),
    ('fab fa-android', 'Android'),
    ('fab fa-apple', 'Apple'),

]

ICON_SOCIAL = [
    ('fab fa-github', 'GitHub'),
    ('fab fa-gitlab', 'GitLab'),
    ('fab fa-bitbucket', 'Bitbucket'),
    ('fab fa-stack-overflow', 'Stack Overflow'),
    ('fab fa-twitter', 'Twitter / X'),
    ('fab fa-linkedin', 'LinkedIn'),
    ('fab fa-discord', 'Discord'),
    ('fab fa-slack', 'Slack'),
    ('fab fa-reddit', 'Reddit'),
    ('fab fa-facebook', 'Facebook'),
    ('fab fa-youtube', 'YouTube'),
    ('fab fa-twitch', 'Twitch'),
    ('fab fa-medium', 'Medium'),
    ('fab fa-dev', 'DEV Community'),
]


class About(models.Model):
    firstname= models.CharField(max_length=30,null=True,blank=True,verbose_name='نام')
    lastname= models.CharField(max_length=30,null=True,blank=True,verbose_name='نام خانوادگی')
    avatar = models.ImageField(upload_to='images/avatars/', verbose_name='آواتار', null=True, blank=True)
    biography = models.TextField(verbose_name='بیوگرافی', null=True, blank=True)
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه', null=True,blank=True)
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    is_active=models.BooleanField(verbose_name='فعال/غیرفعال', default=True)

    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    
    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'

class Social(models.Model):
    parent= models.ForeignKey(About,on_delete=models.CASCADE,verbose_name='پروفایل')
    socialname= models.CharField(max_length=100,choices=ICON_SOCIAL,verbose_name='نام شبکه اجتماعی')
    socialurl= models.URLField(verbose_name='آدرس شبکه اجتماعی')

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"

class Experience(models.Model):
    parent= models.ForeignKey(About,on_delete=models.CASCADE,verbose_name='پروفایل')
    title= models.CharField(max_length=50, verbose_name='عنوان')
    company= models.CharField(max_length=50, verbose_name='نام شرکت یا سازمان')
    description= models.TextField(verbose_name='توضیحات',null=True,blank=True)
    start_date= models.DateField(verbose_name='تاریخ شروع ')
    end_date= models.DateField(verbose_name='تاریخ پایان ', null=True, blank=True)

    class Meta:
        verbose_name = "سابقه"
        verbose_name_plural = "سوابق"

class Education(models.Model):
    parent= models.ForeignKey(About,on_delete=models.CASCADE,verbose_name='پروفایل')
    title= models.CharField(max_length=50, verbose_name='نام اموزشگاه')
    orientation= models.CharField(max_length=50, verbose_name='نام گرایش یا تخصص')
    description= models.TextField(verbose_name='توضیحات',null=True,blank=True)
    gpa= models.CharField(max_length=10,null=True,blank=True,verbose_name='معدل')
    start_date= models.DateField(verbose_name='تاریخ شروع ')
    end_date= models.DateField(verbose_name='تاریخ پایان ', null=True, blank=True)

    class Meta:
        verbose_name = "تحصیل"
        verbose_name_plural = "تحصیلات"

class Skill(models.Model):
    parent= models.ForeignKey(About,on_delete=models.CASCADE,verbose_name='پروفایل')
    title= models.CharField(max_length=100,choices=ICON_SKILL,verbose_name='نام مهارت')

    class Meta:
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت ها"

class Workflow(models.Model):
    parent= models.ForeignKey(About,on_delete=models.CASCADE,verbose_name='پروفایل')
    title= models.CharField(max_length=80, verbose_name='نام مهارت')

    class Meta:
        verbose_name = "مهارت کاری"
        verbose_name_plural = "مهارت های کاری"

class Interests(models.Model):
    parent= models.ForeignKey(About,on_delete=models.CASCADE,verbose_name='پروفایل')
    description= models.TextField(verbose_name='توضیحات',null=True,blank=True)

    class Meta:
        verbose_name = "علاقه مندی"
        verbose_name_plural = "علاقه مندی ها"

class Awards(models.Model):
    parent= models.ForeignKey(About,on_delete=models.CASCADE,verbose_name='پروفایل')
    description= models.TextField(verbose_name='توضیحات',null=True,blank=True)

    class Meta:
        verbose_name = "دست آورد"
        verbose_name_plural = "دست آورد ها"