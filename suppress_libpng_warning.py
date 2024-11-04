# suppress_libpng_warning.py
import warnings

# Ignore the specific 'libpng' iCCP warning
warnings.filterwarnings("ignore", message="iCCP: known incorrect sRGB profile")