/* Include files */

#include "Quadrature_Phase_Shift_Keying_cgxe.h"
#include "m_Jf2lRQWLrP2B1g4UrAzlsF.h"
#include "m_UGsKOob1SZ1GnhcskvCSLB.h"

unsigned int cgxe_Quadrature_Phase_Shift_Keying_method_dispatcher(SimStruct* S,
  int_T method, void* data)
{
  if (ssGetChecksum0(S) == 1017568869 &&
      ssGetChecksum1(S) == 940112189 &&
      ssGetChecksum2(S) == 175103308 &&
      ssGetChecksum3(S) == 3142438572) {
    method_dispatcher_Jf2lRQWLrP2B1g4UrAzlsF(S, method, data);
    return 1;
  }

  if (ssGetChecksum0(S) == 2357531272 &&
      ssGetChecksum1(S) == 679297855 &&
      ssGetChecksum2(S) == 545733252 &&
      ssGetChecksum3(S) == 2219173169) {
    method_dispatcher_UGsKOob1SZ1GnhcskvCSLB(S, method, data);
    return 1;
  }

  return 0;
}
