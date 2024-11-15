start
  break *main+728
  commands
    x/10gx $rsp
    set $local_variable = *(unsigned long long*)($rsp+0x28)
    printf "Current value: %llx\n", $local_variable

    continue
  end
  continue
