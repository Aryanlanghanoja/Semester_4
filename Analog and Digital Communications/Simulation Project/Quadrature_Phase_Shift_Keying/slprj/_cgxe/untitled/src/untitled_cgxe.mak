# ------------------- Required for MSVC nmake ---------------------------------
# This file should be included at the top of a MAKEFILE as follows:


CPU = AMD64

MODEL  = untitled
TARGET = cgxe
MODULE_SRCS 	= m_Jvi3A3pm2laySEv4cTge3F.c
MODEL_SRC	= untitled_cgxe.c
MODEL_REG = untitled_cgxe_registry.c
MAKEFILE    = untitled_cgxe.mak
MATLAB_ROOT	= D:\MATLAB 2024\Setup
BUILDARGS   =

#--------------------------- Tool Specifications ------------------------------
#
#
MSVC_ROOT1 = $(MSDEVDIR:SharedIDE=vc)
MSVC_ROOT2 = $(MSVC_ROOT1:SHAREDIDE=vc)
MSVC_ROOT  = $(MSVC_ROOT2:sharedide=vc)

# Compiler tool locations, CC, LD, LIBCMD:
CC     = cl.exe
LD     = link.exe
LIBCMD = lib.exe
#------------------------------ Include/Lib Path ------------------------------


USER_INCLUDES   =  /I "D:\aryan data\usefull data\semester - 4\analog and digital communications\simulation project\quadrature phase shift keying\slprj\_cgxe\untitled\src" /I "D:\aryan data\usefull data\semester - 4\analog and digital communications\simulation project\quadrature phase shift keying" /I "D:\Aryan Data\Usefull Data\Semester - 4\Analog and Digital Communications\Simulation Project\Quadrature Phase Shift Keying\slprj\_cprj"

MLSL_INCLUDES     = \
    /I "D:\MATLAB 2024\Setup\extern\include" \
    /I "D:\MATLAB 2024\Setup\simulink\include" \
    /I "D:\MATLAB 2024\Setup\rtw\c\src"
COMPILER_INCLUDES = /I "$(MSVC_ROOT)\include"

THIRD_PARTY_INCLUDES   =  /I "D:\Aryan Data\Usefull Data\Semester - 4\Analog and Digital Communications\Simulation Project\Quadrature Phase Shift Keying\slprj\_cgxe\untitled\src" /I "D:\Aryan Data\Usefull Data\Semester - 4\Analog and Digital Communications\Simulation Project\Quadrature Phase Shift Keying"
INCLUDE_PATH = $(MLSL_INCLUDES) $(USER_INCLUDES) $(THIRD_PARTY_INCLUDES)
LIB_PATH     = "$(MSVC_ROOT)\lib"
CFLAGS = /c /Zp8 /GR /w /EHs /D_CRT_SECURE_NO_DEPRECATE /D_SCL_SECURE_NO_DEPRECATE /D_SECURE_SCL=0 /DMX_COMPAT_64 /DMATLAB_MEXCMD_RELEASE=R2018a /DMATLAB_MEX_FILE /nologo /MD   
LDFLAGS = /nologo /dll /MANIFEST /OPT:NOREF /export:mexFunction /export:mexfilerequiredapiversion  
#----------------------------- Source Files -----------------------------------

USER_OBJS =

AUX_SRCS = D:\MATLAB 2024\Setup\extern\version\c_mexapi_version.c  

REQ_SRCS  = $(MODEL_SRC) $(MODEL_REG) $(MODULE_SRCS) $(AUX_SRCS)
REQ_OBJS = $(REQ_SRCS:.cpp=.obj)
REQ_OBJS2 = $(REQ_OBJS:.c=.obj)
OBJS = $(REQ_OBJS2) $(USER_OBJS) $(AUX_ABS_OBJS)
OBJLIST_FILE = untitled_cgxe.mol
TMWLIB = "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmx.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmex.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmat.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libfixedpoint.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libut.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmwmathutil.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libemlrt.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmwcgxert.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmwcgxeooprt.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmwslexec_simbridge.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmwslccrt.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmwstringutil.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libcovrt.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmwsl_sfcn_cov_bridge.lib" "D:\MATLAB 2024\Setup\extern\lib\win64\microsoft\libmwdsp_halidesim.lib" 
THIRD_PARTY_LIBS = 

#--------------------------------- Rules --------------------------------------

MEX_FILE_NAME_WO_EXT = $(MODEL)_$(TARGET)
MEX_FILE_NAME = $(MEX_FILE_NAME_WO_EXT).mexw64
all : $(MEX_FILE_NAME) 


$(MEX_FILE_NAME) : $(MAKEFILE) $(OBJS)
	@echo ### Linking ...
	$(LD) $(LDFLAGS) /OUT:$(MEX_FILE_NAME) /map:"$(MEX_FILE_NAME_WO_EXT).map" $(TMWLIB) $(THIRD_PARTY_LIBS) @$(OBJLIST_FILE)
	@echo ### Created $@

.c.obj :
	@echo ### Compiling "$<"
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "$<"

.cpp.obj :
	@echo ### Compiling "$<"
	$(CC) $(CFLAGS) $(INCLUDE_PATH) "$<"

