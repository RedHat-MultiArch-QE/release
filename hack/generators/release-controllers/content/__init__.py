# pylint: disable=R0801

from .osd_rc_deployments import add_osd_rc_deployments
from .osd_rc_rbac import add_osd_rc_service_account_resources
from .art_publish_permissions import add_art_publish
from .art_namespaces_config_updater import add_art_namespace_config_updater_rbac
from .art_namespaces_rbac import add_imagestream_namespace_rbac
from .redirect_and_files_cache_resources import add_redirect_and_files_cache_resources
from .art_rpm_mirroring_services import add_rpm_mirror_service
from .art_input_images import add_golang_release_builders, add_golang_builders, add_base_image_builders
