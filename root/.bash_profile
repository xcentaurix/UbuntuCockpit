#!/bin/bash
export PATH=/usr/share/opkg/intercept:/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/media/hdd/ubuntu/root:~/git/tools:~/git/dev/SkinForge
if [ ! -f /usr/bin/enigma2 ]; then
    export PS1='(chroot) \u@\h:\w$ '
else
    export PS1='\u@\h:\w$ '
fi
if [ -d /root/venv/bin ]; then
    source ~/venv/bin/activate
    cd /root/git/dev
else
    cd /
    if [ ! -e /git ]; then
        ln -s ~/git
    fi    
    cd ~/logs
fi
alias tools="cd ~/git/tools"
alias dev="cd ~/git/dev"
alias rel="cd ~/git/rel"
alias wiki="cd ~/git/wiki"
alias root="cd ~"
alias logs="cd ~/logs"
alias skin="cd skin/default"

for dir in "$HOME/git/dev/"*; do
    # echo $dir
    domain=$(~/git/tools/getdomain $dir)
    # echo $domain
    lower_domain="${domain,,}"
    # echo $lower_domain
    # echo alias $lower_domain="cd ~/git/dev/$domain/src"
    alias $lower_domain="cd ~/git/dev/$domain/src"
    # echo alias $domain="cd ~/git/rel/$domain/src"
    alias $domain="cd ~/git/rel/$domain/src"
done

if [ -f /bin/ubuntu ]; then
    ubuntu
fi
