from . import *

logout_bp = Blueprint('logout', __name__)
@logout_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Cierre de sesión exitoso"}), 200