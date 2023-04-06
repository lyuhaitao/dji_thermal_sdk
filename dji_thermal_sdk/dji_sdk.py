# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core_dji.ipynb.

# %% auto 0
__all__ = ['DIRP_PSEUDO_COLOR_WHITEHOT', 'DIRP_PSEUDO_COLOR_FULGURITE', 'DIRP_PSEUDO_COLOR_IRONRED', 'DIRP_PSEUDO_COLOR_HOTIRON',
           'DIRP_PSEUDO_COLOR_MEDICAL', 'DIRP_PSEUDO_COLOR_ARCTIC', 'DIRP_PSEUDO_COLOR_RAINBOW1',
           'DIRP_PSEUDO_COLOR_RAINBOW2', 'DIRP_PSEUDO_COLOR_TINT', 'DIRP_PSEUDO_COLOR_BLACKHOT',
           'DIRP_PSEUDO_COLOR_NUM', 'DIRP_PSEUDO_COLOR_LUT_DEPTH', 'DIRP_SUCCESS', 'DIRP_ERROR_MALLOC',
           'DIRP_ERROR_POINTER_NULL', 'DIRP_ERROR_INVALID_PARAMS', 'DIRP_ERROR_INVALID_RAW',
           'DIRP_ERROR_INVALID_HEADER', 'DIRP_ERROR_INVALID_CURVE', 'DIRP_ERROR_RJPEG_PARSE', 'DIRP_ERROR_SIZE',
           'DIRP_ERROR_INVALID_HANDLE', 'DIRP_ERROR_FORMAT_INPUT', 'DIRP_ERROR_FORMAT_OUTPUT',
           'DIRP_ERROR_UNSUPPORTED_FUNC', 'DIRP_ERROR_NOT_READY', 'DIRP_ERROR_ACTIVATION', 'DIRP_ERROR_INVALID_INI',
           'DIRP_ERROR_INVALID_SUB_DLL', 'DIRP_ERROR_ADVANCED', 'DIRP_HANDLE', 'dirp_api_version_t', 'dirp_color_bar_t',
           'dirp_enhancement_params_t', 'dirp_isotherm_t', 'dirp_isp_pseudo_color_lut_t',
           'dirp_measurement_params_range_t', 'dirp_measurement_params_t', 'dirp_resolution_t', 'dirp_rjpeg_version_t',
           'set_dirp_dll', 'dirp_create_from_rjpeg', 'dirp_destroy', 'dirp_get_api_version', 'dirp_get_color_bar',
           'dirp_get_color_bar_adaptive_params', 'dirp_get_enhancement_params', 'dirp_get_isotherm',
           'dirp_get_measurement_params', 'dirp_get_measurement_params_range', 'dirp_get_original_raw',
           'dirp_get_pseudo_color', 'dirp_get_pseudo_color_lut', 'dirp_get_rjpeg_resolution', 'dirp_get_rjpeg_version',
           'dirp_measure', 'dirp_measure_ex', 'dirp_process', 'dirp_process_strech', 'dirp_set_color_bar',
           'dirp_set_enhancement_params', 'dirp_set_isotherm', 'dirp_set_logger_file', 'dirp_set_measurement_params',
           'dirp_set_pseudo_color', 'dirp_set_verbose_level', 'get_pseudo_color']

# %% ../nbs/00_core_dji.ipynb 3
import ctypes as CT
from ctypes import *

# %% ../nbs/00_core_dji.ipynb 4
_libdirp = ""
# dirp_pseudo_color_e
DIRP_PSEUDO_COLOR_WHITEHOT   = 0
DIRP_PSEUDO_COLOR_FULGURITE  = 1
DIRP_PSEUDO_COLOR_IRONRED    = 2
DIRP_PSEUDO_COLOR_HOTIRON    = 3
DIRP_PSEUDO_COLOR_MEDICAL    = 4
DIRP_PSEUDO_COLOR_ARCTIC     = 5
DIRP_PSEUDO_COLOR_RAINBOW1   = 6
DIRP_PSEUDO_COLOR_RAINBOW2   = 7
DIRP_PSEUDO_COLOR_TINT       = 8
DIRP_PSEUDO_COLOR_BLACKHOT   = 9
DIRP_PSEUDO_COLOR_NUM        = 10

# palette look_up table
DIRP_PSEUDO_COLOR_LUT_DEPTH = 256

# dirp_ret_code_e
DIRP_SUCCESS = 0
DIRP_ERROR_MALLOC = -1
DIRP_ERROR_POINTER_NULL = -2
DIRP_ERROR_INVALID_PARAMS = -3,
DIRP_ERROR_INVALID_RAW = -4
DIRP_ERROR_INVALID_HEADER = -5
DIRP_ERROR_INVALID_CURVE = -6
DIRP_ERROR_RJPEG_PARSE = -7
DIRP_ERROR_SIZE = -8
DIRP_ERROR_INVALID_HANDLE = -9
DIRP_ERROR_FORMAT_INPUT = -10
DIRP_ERROR_FORMAT_OUTPUT = -11,
DIRP_ERROR_UNSUPPORTED_FUNC = -12
DIRP_ERROR_NOT_READY = -13
DIRP_ERROR_ACTIVATION = -14
DIRP_ERROR_INVALID_INI = -15
DIRP_ERROR_INVALID_SUB_DLL = -16
DIRP_ERROR_ADVANCED = -32

# Initialize the handle of a r-jpeg image.
DIRP_HANDLE = CT.c_void_p()

# %% ../nbs/00_core_dji.ipynb 5
class dirp_api_version_t(CT.Structure):
    '''
    API version structure definition
    '''
    _fields_ = [("api", CT.c_uint32), ("magic", CT.c_char * 8)]
#
class dirp_color_bar_t(Structure):
    '''
    Color bar parameters structure definition
    '''
    _fields_ = [("manual_enable", CT.c_bool), ("high", CT.c_float), ("low", CT.c_float)]
#
class dirp_enhancement_params_t(Structure):
    '''
    Image enhancement parameteres structure definition
    '''
    _fields_ = [("brightness", CT.c_int32)]
#
class dirp_isotherm_t (Structure):
    '''
    Isotherm parameters structure definition
    '''
    _fields_ = [("enable", CT.c_bool), ("high", CT.c_float), ("low", CT.c_float)]
#
class dirp_isp_pseudo_color_lut_t (Structure):
    '''
    Pseudo color LUT array structure definition
    '''
    _fields_ = [("red", (CT.c_uint8 * DIRP_PSEUDO_COLOR_NUM) * DIRP_PSEUDO_COLOR_LUT_DEPTH),
                ("green",(CT.c_uint8 * DIRP_PSEUDO_COLOR_NUM) * DIRP_PSEUDO_COLOR_LUT_DEPTH ),
                ("blue",(CT.c_uint8 * DIRP_PSEUDO_COLOR_NUM) * DIRP_PSEUDO_COLOR_LUT_DEPTH )
               ]
#
class _distance(Structure):
    _fields_ = [("min", CT.c_float), ("max", CT.c_float)]
#
class _humidity(Structure):
    _fields_ = [("min", CT.c_float), ("max", CT.c_float)]
#
class _emissivity(Structure):
    _fields_ = [("min", CT.c_float), ("max", CT.c_float)]
#
class _reflection(Structure):
    _fields_ = [("min", CT.c_float), ("max", CT.c_float)]
#
class dirp_measurement_params_range_t(Structure):
    '''
    Range of temperature measurement parameteres structure definition
    '''
    _fields_ = [("distance", _distance),
                ("humidity", _humidity),
                ("emissivity", _emissivity),
                ("reflection", _reflection)
               ]
#
class dirp_measurement_params_t(Structure):
    '''
    Customize temperature measurement parameteres structure definition
    '''
    _fields_ = [("distance", c_float),
                ("humidity", c_float),
                ("emissivity", c_float),
                ("reflection", c_float)
               ]
#
class dirp_resolution_t(Structure):
    '''
    The image size structure definition
    '''
    _fields_ = [("width", CT.c_int32),("height", CT.c_int32)]
#
class dirp_rjpeg_version_t (Structure):
    '''
    R-JPEG version structure definition
    '''
    _fields_ = [("rjpeg", CT.c_uint32),("header", CT.c_uint32),("curve", CT.c_uint32)]
    pass

# %% ../nbs/00_core_dji.ipynb 6
try:
    _libdirp = cdll.LoadLibrary("./libdirp.dll")
    DJI.set_dirp_dll(_libdirp)
except FileNotFoundError as err:
    print(err)

# %% ../nbs/00_core_dji.ipynb 7
def set_dirp_dll(libdirp):
    global _libdirp
    _libdirp = libdirp
    pass

def _getFunHandleFromDJIDll(dll_handle_str, fun_name_str):
    s = "{}.{}".format(dll_handle_str,fun_name_str)
    try:
        fun = eval(s)
        return fun
    except AttributeError as err:
        e = f"{dll_handle_str}.dll has no function '{fun_name_str}'"
        print(e)
        return -1
    pass

# %% ../nbs/00_core_dji.ipynb 8
def dirp_create_from_rjpeg(data, size, ph):
    '''
    Parameters:
        [in] data: R-JPEG binary data buffer pointer
        [in] size: R-JPEG binary data buffer size in bytes
        [out]ph  : DIRP API handle pointer 
            - reminder: use two-level pointer to assign value to one-level pointer
    Return:
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp","dirp_create_from_rjpeg")
    ret = fun(data, size, ph)
    return ret
    pass
def dirp_destroy(ph):
    '''
    Parameters:
        [in]ph: DIRP API handle
    Return:
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_destroy")
    ret = fun(ph)
    return ret
    pass
def dirp_get_api_version(version):
    '''
    Parameters:
        [out] version DIRP API version information pointer
    Return:
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_api_version")
    ret = fun(version)
    return ret
    pass
#
def dirp_get_color_bar(h, color_bar):
    '''
    Parameters:
        [in]  h: DIRP API handle
        [out] color_bar: ISP color bar parameters pointer
    Return:
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_color_bar")
    ret = fun(h, color_bar)
    return ret
    pass
#

def dirp_get_color_bar_adaptive_params(h, color_bar):
    '''
    Get adaptive ISP color bar parameters in automatic mode.
    In color bar automatic mode : manual_enable in dirp_color_bar_t is set as false. 
    The inner ISP algorithm will calculate the best range values for color bar. 
    Before calling this API you should call dirp_process once at least. 
    And if any processing or measurement parameters had been changed, 
    you should also call dirp_process again for getting new color bar adaptive parameters. 
    In the above calling dirp_process, manual_enable in dirp_color_bar_t must be set as false.

    Parameters
        [in] h: DIRP API handle
        [out] color_bar: ISP color bar parameters pointer

    Return:
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_color_bar_adaptive_params")
    ret = fun(h, color_bar)
    return ret
    pass
#
#
def dirp_get_enhancement_params(h, enhancement_params):
    '''
    Get orignial/custom ISP enhancement parameters.
    Parameters:
        [in] h: DIRP API handle
        [out] enhancement_params ISP enhancement parameters pointer

    Return:
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_enhancement_params")
    ret = fun(h, enhancement_params)
    return ret
    pass
#
def dirp_get_isotherm(h, isotherm):
    '''
    Get orignial/custom ISP isotherm parameters.
    Parameters
        [in]h: DIRP API handle
        [out]isotherm: ISP isotherm parameters pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_isotherm")
    ret = fun(h, isotherm)
    return ret
#
def dirp_get_measurement_params(h, measurement_params):
    '''
    Get orignial/custom temperature measurement parameters.
    Parameters
        [in] h: DIRP API handle
        [out] measurement_params: Temperature measurement parameters pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_measurement_params")
    ret = fun(h, measurement_params)
    return ret
#
def dirp_get_measurement_params_range(h, params_range):
    '''
    Get range of temperature measurement parameters that user can set.
    Parameters
        [in] h: DIRP API handle
        [out] params_range: Temperature measurement parameters range pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_measurement_params_range")
    ret = fun(h, params_range)
    return ret
#
def dirp_get_original_raw(h, raw_image, size):
    '''
    Get original RAW binary data from R-JPEG.
    Parameters
        [in]h:DIRP API handle
        [out]raw_image:Original RAW image data buffer pointer
        [in]size:Original RAW image data buffer size in bytes
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_original_raw")
    ret = fun(h, raw_image, size)
    return ret
#
def dirp_get_pseudo_color(h, pseudo_color):
    '''
    Get orignial/custom ISP pseudo color type.
    Parameters
        [in]h: DIRP API handle
        [out]pseudo_color	ISP pseudo color type pointer dirp_pseudo_color_e
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_pseudo_color")
    ret = fun(h, pseudo_color)
    return ret
#
def dirp_get_pseudo_color_lut(h, pseudo_lut):
    '''
    Get ISP pseudo color LUT.
    Parameters
        [in]h: DIRP API handle
        [out]pseudo_lut: ISP pseudo color LUT pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_pseudo_color_lut")
    ret = fun(h, pseudo_lut)
    return ret
#
def dirp_get_rjpeg_resolution(h, rjpeg_info):
    '''
    Get R-JPEG image resolution information.
    Parameters
        [in]h: DIRP API handle
        [out]rjpeg_info: R-JPEG basic information pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_rjpeg_resolution")
    ret = fun(h, rjpeg_info)
    return ret
#
def dirp_get_rjpeg_version(h, version):
    '''
    Get R-JPEG version.
    Parameters
        [in]h:DIRP API handle
        [out]version: R-JPEG version information pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_get_rjpeg_version")
    ret = fun(h, version)
    return ret
#
def dirp_measure(h, temp_image, size):
    '''
    Measure temperature of whole thermal image with RAW data in R-JPEG.
    Each INT16 pixel value represents ten times the temperature value in Celsius. 
    In other words, each LSB represents 0.1 degrees Celsius. 
    The custom measurement parameters can be modifed by this API:dirp_set_measurement_params
    Parameters
        [in]h:DIRP API handle
        [out]temp_image:Temperature image data buffer pointer
        [in]size:Temperature image data buffer size in bytes
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_measure")
    ret = fun(h, temp_image, size)
    return ret
#
def dirp_measure_ex(h, temp_image, size):
    '''
    Measure temperature of whole thermal image with RAW data in R-JPEG.
    Each FLOAT32 pixel value represents the real temperature in Celsius. 
    The custom measurement parameters can be modifed by this API:

    dirp_set_measurement_params
    Parameters
        [in]h:DIRP API handle
        [out]temp_image:Temperature image data buffer pointer
        [in]size:Temperature image data buffer size in bytes
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_measure_ex")
    ret = fun(h, temp_image, size)
    return ret
#
def dirp_process(h, color_image, size):
    '''
    Run ISP algorithm with RAW data in R-JPEG and output RGB pseudo color image.
    The ISP configurable parameters can be modifed by these APIs:
        dirp_set_enhancement_params
        dirp_set_isotherm
        dirp_set_color_bar
        dirp_set_pseudo_color
    Parameters
        [in]h:DIRP API handle
        [out]color_image:Color image data buffer pointer
        [in]size:Color image data buffer size in bytes.
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_process")
    ret = fun(h, color_image, size)
    return ret
#
def dirp_process_strech(h, strech_image, size):
    '''
    Run ISP strech algorithm with RAW data in R-JPEG and output FLOAT32 streching image.
    The ISP strech configurable parameters can be modifed by these APIs:

        dirp_set_enhancement_params
        dirp_set_isotherm
        dirp_set_color_bar
    Parameters
        [in]h:DIRP API handle
        [out]strech_image:Strech image data buffer pointer
        [in]size:Strech image data buffer size in bytes.
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_process_strech")
    ret = fun(h, strech_image, size)
    return ret
#
def dirp_set_color_bar(h, color_bar):
    '''
    Set custom ISP color bar parameters.
    Parameters
        [in]h:DIRP API handle
        [in]color_bar:ISP color bar parameters pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_set_color_bar")
    ret = fun(h, color_bar)
    return ret
#
def dirp_set_enhancement_params(h, enhancement_params):
    '''
    Set custom ISP enhancement parameters.
    Parameters
        [in]h:DIRP API handle
        [in]enhancement_params:ISP enhancement parameters pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_set_enhancement_params")
    ret = fun(h, enhancement_params)
    return ret
#
def dirp_set_isotherm(h, isotherm):
    '''
    Set custom ISP isotherm parameters.
    Parameters
        [in]h:DIRP API handle
        [in]isotherm:ISP isotherm parameters pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_set_isotherm")
    ret = fun(h, isotherm)
    return ret
#
def dirp_set_logger_file(file_name):
    '''
    Set external logger file.
    Parameters
        [in]file_name:File name which save log information. Set it as nullptr if you want print log on console.

    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_set_logger_file")
    ret = fun(file_name)
    return ret
#
def dirp_set_measurement_params(h, measurement):
    '''
    Set custom temperature measurement parameters.
    Parameters
        [in]h:DIRP API handle
        [in]measurement_params:Temperature measurement parameters pointer
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_set_measurement_params")
    ret = fun(h, measurement)
    return ret
#
def dirp_set_pseudo_color(h, pseudo_color):
    '''
    Set custom ISP pseudo color type.
    Parameters
        [in]h:DIRP API handle
        [in]pseudo_color:ISP pseudo color type dirp_pseudo_color_e
    Returns
        int return code dirp_ret_code_e
    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_set_pseudo_color")
    ret = fun(h, pseudo_color)
    return ret
#
def dirp_set_verbose_level(level):
    '''
    Set log print level.
    Parameters
        [in]level:Log pring level dirp_verbose_level_e

    '''
    fun = _getFunHandleFromDJIDll("_libdirp", "dirp_set_verbose_level")
    ret = fun(level)
    return ret
    

# %% ../nbs/00_core_dji.ipynb 9
def get_pseudo_color():
    "return the pseudo color dictionary."
    pseudo_color = {'white_hot':0, 'fulgurite':1, 'iron_red':2, 'hot_iron':3, 'medical':4,
                'arctic': 5, 'rainbow1':6, 'rainbow2':7, 'Tint':8, 'black_hot':9
               }
    return pseudo_color
