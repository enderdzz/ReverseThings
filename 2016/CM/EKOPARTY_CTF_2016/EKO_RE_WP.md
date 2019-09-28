# Reverse Write Up:

1.

A ver easy calc problem.
The answer is the sum of 1 to 2666.
python -c "print sum(range(1, 2666))"

2.

A C# prog.
A reverse string "t#hs_siht_kc#f"

EKO{f#ck_this_sh#t}

*Attach: Program.cs*

3.

```
Program.check_regex("^.{40}$", input)                     /// 任意40个字符
 && Program.check_regex("\\w{3}\\{.*\\}", input)		  /// EKO{}  \w{3}\{.*\}
 && Program.check_regex("_s.*e_", input)				  /// _s.eee_
 && Program.check_regex("\\{o{2}O{2}o{2}", input)		  /// \{ooOOooOO\}
 && Program.check_regex("O{2}o{2}O{2}\\}", input)		  ///
 && Program.check_regex("sup3r_r3g3x_challenge", input)
```
EKO{ooOOoo_sup3r_r3g3x_challenge_OOooOO}

4.

I just download the software named as "ViewSavF" to open this .SAVF file and then see the flag.

5.
[\*]

After the contest I was just known the file can be read in the format of IBM's EBCDIC encoding. And this encoding format can be set in the TCP stream packets.
So I just use the 'nc' tool to send local loopback data packets and capture them :

receiver:

`➜  ~ nc -l -vv -p 2333 > CHALLENGE2.MBR`

sender:

`➜  ~ nc -vv 127.0.0.1 2333 < ~/tmp/CHALLENGE2.MBR
Connection to 127.0.0.1 2333 port [tcp/*] succeeded!
`

and from the wireshark you can see the corresponding packet. Then follow the TCP stream and choose the EBCDIC encoding. Find this familiar string:
```bash
In [3]: ss = '${}wtf_mgpENTER SECRET KEYCHECKING SECRET KEY._ytrOKAY! GRAB YOUR FLAGapoke_t33l_l0b0c{O..OH SNAP, YOUR KEY IS'

In [4]: print ss[::-1]
SI YEK RUOY ,PANS HO..O{c0b0l_l33t_ekopaGALF RUOY BARG !YAKOrty_.YEK TERCES GNIKCEHCYEK TERCES RETNEpgm_ftw}{$
```
the flag is EKO{c0b0l_l33t_ekoparty_pgm_ftw}

*Attachment: flag.png*

6.
[\*]
