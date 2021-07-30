from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class ExpertandLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is Expert."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_Expert:
            return redirect("healthcare:healthcare-patient_list")
        return super().dispatch(request, *args, **kwargs)