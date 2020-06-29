from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    image_name = models.CharField(max_length=30)
    image_desc = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model instance."""
        return self.image_name

    def save_image(self):
        """Save image to the database."""
        self.save()

    def delete_image(self):
        """Delete image from the database."""
        self.delete()

    def update_image(self, **kwargs):
        """Update image in the database."""
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.save()
