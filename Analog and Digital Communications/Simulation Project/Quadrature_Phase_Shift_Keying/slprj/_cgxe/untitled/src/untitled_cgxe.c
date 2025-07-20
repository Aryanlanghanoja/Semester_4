/* Include files */

#include "untitled_cgxe.h"
#include "m_Jvi3A3pm2laySEv4cTge3F.h"

unsigned int cgxe_untitled_method_dispatcher(SimStruct* S, int_T method, void
  * data)
{
  if (ssGetChecksum0(S) == 2563022521 &&
      ssGetChecksum1(S) == 4101697964 &&
      ssGetChecksum2(S) == 3830063142 &&
      ssGetChecksum3(S) == 2626633638) {
    method_dispatcher_Jvi3A3pm2laySEv4cTge3F(S, method, data);
    return 1;
  }

  return 0;
}
