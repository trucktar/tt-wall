from cloudinary.models import CloudinaryField
from django.db import models


class CrudMixin:
    def save_model(self):
        """Save model instance to the database."""
        self.save()

    def delete_model(self):
        """Delete model instance from the database."""
        self.delete()

    def update_model(self, **kwargs):
        """Update model instance in the database."""
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.save()


class Category(models.Model, CrudMixin):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Location(models.Model, CrudMixin):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name


class Image(models.Model, CrudMixin):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_desc = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model instance."""
        return self.image_name

    @classmethod
    def get_image_by_id(cls, image_id):
        """Get image from database by id."""
        image = cls.objects.get(pk=image_id)
        return image

    @classmethod
    def search_by_category(cls, category):
        """Find image from database by category."""
        images = cls.objects.filter(category__category_name=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        """Filter images based on location."""
        images = cls.objects.filter(location__location_name=location)
        return images
