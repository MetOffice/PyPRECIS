cat > stash_select << eof
begin
  stash=(3236, 5216, 16222)
  T1>={1981/01/01}
  T1<{1984/01/01}
end
eof

moo select stash_select moose:/crum/cahpa/apm.pp /project/precis/worksheets/data/pp/cahpa/.
moo select stash_select moose:/crum/cahpb/apm.pp /project/precis/worksheets/data/pp/cahpb/.
