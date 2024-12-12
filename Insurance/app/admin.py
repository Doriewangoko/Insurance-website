from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import FileUpload
from .models import Product, CartItem


# Use Django's built-in UserAdmin for the default User model
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register the default User model with the updated UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# ModelAdmin class for FileUpload
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded_at', 'file_size')
    list_filter = ('uploaded_at',)
    search_fields = ('file',)
    ordering = ('-uploaded_at',)

    def file_name(self, obj):
        return obj.file.name

    def file_size(self, obj):
        return f"{obj.file.size / 1024:.2f} KB"

    file_size.short_description = 'File Size'

# Register FileUpload model with custom admin options
admin.site.register(FileUpload, FileUploadAdmin)

# ModelAdmin classes for Product and CartItem
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')