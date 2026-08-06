from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


def optimize_image(image_field, max_size=(1200, 1200), quality=80):
    """
    Resizes and compresses an uploaded image in-place.
    Call this inside a model's save() method before super().save().
    """
    if not image_field:
        return image_field

    img = Image.open(image_field)

    # Convert to RGB if needed (handles PNG with transparency, etc.)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')

    # Resize only if bigger than max_size — never upscale
    img.thumbnail(max_size, Image.LANCZOS)

    output = BytesIO()
    img.save(output, format='JPEG', quality=quality, optimize=True)
    output.seek(0)

    return InMemoryUploadedFile(
        output, 'ImageField',
        f"{image_field.name.split('.')[0]}.jpg",
        'image/jpeg',
        sys.getsizeof(output),
        None
    )