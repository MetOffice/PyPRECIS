cat > stash_select << eof
begin
  stash=(3236, 5216)
  T1>={2021/01/01}
  T1<{2051/01/01}
end
eof

# Stash options are: 3236 = Temperature at surface
#					 5216 = Total precipitation rate
#					 16222 = PMSL

moo select stash_select moose:/crum/cahpa/apm.pp /project/precis/worksheets/data/pp/cahpa/.
moo select stash_select moose:/crum/cahpb/apm.pp /project/precis/worksheets/data/pp/cahpb/.
