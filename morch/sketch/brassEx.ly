\version "2.22.0"
\language "english"

iygh_call_aa = { r8 bf8-. d'8 bf8 f2-- }
iygh_call_ab = { r8 bf8-. g'8 bf8 f2-- }
iygh_call_ba = { r8 bf8-. a8 bf8 c'2-- }
iygh_call_bb = { r8 f8-. bf8 c'8 d'2-- }
iygh_call_bc = { r1 } 

iygh_resp_aa = { r2 r8 bf8-. d'8 bf8 }
iygh_resp_ab = { f2-- r8 bf8-. g'8 bf8 } 
iygh_resp_ba = { f2-- r8 bf8-. a8 bf8 } 
iygh_resp_bb = { c'2-- r8 f8-. bf8 c'8 } 
iygh_resp_bc = { d'2-- r2 } 


hrn_one = {
  \iygh_call_aa
  \iygh_call_ab
  \iygh_call_ba
  \iygh_call_bb
  \iygh_call_bc
}

hrn_three = {
  \iygh_resp_aa
  \iygh_resp_ab
  \iygh_resp_ba
  \iygh_resp_bb
  \iygh_resp_bc
}
