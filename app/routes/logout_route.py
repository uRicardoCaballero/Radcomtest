from . import *
from app.models import * 
       
logout_bp = Blueprint('logout', __name__)
@logout_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    if not current_user.is_authenticated:
        return jsonify({"message": "User not logged in"}), 401
    logout_user()
    return jsonify({"message": "Cierre de sesión exitoso"}), 200