from django.db import models
from django.utils.translation import ugettext_lazy as _
from PIL import Image
from django.core.validators import RegexValidator

# Create your models here.
class About(models.Model):
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    dp = models.ImageField(_("Profile Image"), default='user.png',upload_to='Portfolio')
    address_street = models.CharField(_("Street Address"), max_length=50)
    full_address = models.CharField(_("Full Address"), max_length=200)
    short_description = models.TextField(_("Admin Short Description"))
    interests = models.TextField(_("Interests"))
    cv = models.FileField(_("CV"), upload_to='Portfolio', max_length=500)
    contact_qr = models.ImageField(_("Contact QR Image"), upload_to='Portfolio')

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.dp.path)
        if img.height > 1000 or img.width > 1000:
            output_size= (1000,1000)
            img.thumbnail(output_size)
            img.save(self.dp.path)
        img = Image.open(self.contact_qr.path)
        if img.height > 600 or img.width > 600:
            output_size= (600,600)
            img.thumbnail(output_size)
            img.save(self.contact_qr.path)

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("About Admin")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("About_detail", kwargs={"pk": self.pk})

class AdminContact(models.Model):
    mobile_num_regex = RegexValidator(regex="^[0-9]{9,15}$", message="Entered mobile number isn't in a right format!")
    contact = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True, null=True)

    class Meta:
        verbose_name = _("Admin Contact")
        verbose_name_plural = _("Admin Contacts")

    def __str__(self):
        return self.contact

    def get_absolute_url(self):
        return reverse("AdminContact_detail", kwargs={"pk": self.pk})

class AdminEmail(models.Model):
    email = models.EmailField(_("Email"), max_length=254)

    class Meta:
        verbose_name = _("Admin Email")
        verbose_name_plural = _("Admin Emails")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("AdminEmail_detail", kwargs={"pk": self.pk})

class SocialIcon(models.Model):
    name = models.CharField(_("Identifier Name"), max_length=50)
    fas_iframe = models.CharField(_("Font Awesome Iframe Code"), max_length=100)
    link = models.CharField(_("Link to Website"), max_length=500)

    class Meta:
        verbose_name = _("Social Icon")
        verbose_name_plural = _("SocialIcons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SocialIcon_detail", kwargs={"pk": self.pk})

class Experience(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    from_date = models.DateField(_("From Date"), auto_now=False, auto_now_add=False)
    to_date = models.DateField(_("To Date"), auto_now=False, auto_now_add=False)
    worked_organization = models.CharField(_("Where You Worked"), max_length=100)
    short_info = models.TextField(_("Short Information About Work"))

    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")

    def __str__(self):
        return self.worked_organization

    def get_absolute_url(self):
        return reverse("Experience_detail", kwargs={"pk": self.pk})

class Education(models.Model):
    academy = models.CharField(_("School/College/University"), max_length=50)
    from_date = models.DateField(_("From Date"), auto_now=False, auto_now_add=False)
    to_date = models.DateField(_("From Date"), auto_now=False, auto_now_add=False)
    faculty = models.CharField(_("Faculty"), max_length=100)
    subject = models.CharField(_("Subject"), max_length=100)
    per_gpa = models.CharField(_("Percentage or GPA"), max_length=50)

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")
        ordering = ['-to_date']

    def __str__(self):
        return self.academy

    def get_absolute_url(self):
        return reverse("Education_detail", kwargs={"pk": self.pk})

class ProgrammingLanguagesAndTools(models.Model):
    iframe = models.CharField(_("Font Awesome Iframe"), max_length=80)
    title = models.CharField(_("Title"), max_length=100)

    class Meta:
        verbose_name = _("Programming Languages And Tool")
        verbose_name_plural = _("Programming Languages And Tools")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ProgrammingLanguagesAndTools_detail", kwargs={"pk": self.pk})

class Project(models.Model):
    name = models.CharField(_("Project Name"), max_length=50)
    short_info = models.TextField(_("Short Info"), null=True, blank=True)
    short_desc = models.TextField(_("Short Description"), null=True, blank=True)
    remarks = models.TextField(_("Short Description"), null=True, blank=True)
    project_link = models.CharField(_("Link to project"), max_length=500, blank=True, null=True)
    hosted_on = models.CharField(_("Hosted On"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Project_detail", kwargs={"pk": self.pk})


