FasdUAS 1.101.10   ��   ��    k             l      ��  ��    � �

This Apple script will resize any program window to an exact size and the window is then moved to the center of your screen. Specify the program name, height and width below and run the script.

Written by Amit Agarwal on December 10, 2013

     � 	 	� 
 
 T h i s   A p p l e   s c r i p t   w i l l   r e s i z e   a n y   p r o g r a m   w i n d o w   t o   a n   e x a c t   s i z e   a n d   t h e   w i n d o w   i s   t h e n   m o v e d   t o   t h e   c e n t e r   o f   y o u r   s c r e e n .   S p e c i f y   t h e   p r o g r a m   n a m e ,   h e i g h t   a n d   w i d t h   b e l o w   a n d   r u n   t h e   s c r i p t . 
 
 W r i t t e n   b y   A m i t   A g a r w a l   o n   D e c e m b e r   1 0 ,   2 0 1 3 
 
   
  
 l     ��������  ��  ��        l     ����  r         m        �    G o o g l e   C h r o m e  o      ���� 0 theapp theApp��  ��        l    ����  r        m    ����8  o      ���� 0 	appheight 	appHeight��  ��        l    ����  r        m    	�����  o      ���� 0 appwidth appWidth��  ��        l     ��������  ��  ��         l    !���� ! O     " # " r     $ % $ n     & ' & 1    ��
�� 
pbnd ' n     ( ) ( m    ��
�� 
cwin ) 1    ��
�� 
desk % o      ���� $0 screenresolution screenResolution # m     * *�                                                                                  MACS  alis    @  Macintosh HD                   BD ����
Finder.app                                                     ����            ����  
 cu             CoreServices  )/:System:Library:CoreServices:Finder.app/    
 F i n d e r . a p p    M a c i n t o s h   H D  &System/Library/CoreServices/Finder.app  / ��  ��  ��      + , + l     ��������  ��  ��   ,  - . - l   ! /���� / r    ! 0 1 0 n     2 3 2 4    �� 4
�� 
cobj 4 m    ����  3 o    ���� $0 screenresolution screenResolution 1 o      ���� 0 screenwidth screenWidth��  ��   .  5 6 5 l  " ( 7���� 7 r   " ( 8 9 8 n   " & : ; : 4   # &�� <
�� 
cobj < m   $ %����  ; o   " #���� $0 screenresolution screenResolution 9 o      ���� 0 screenheight screenHeight��  ��   6  = > = l     ��������  ��  ��   >  ?�� ? l  ) ~ @���� @ O   ) ~ A B A k   0 } C C  D E D I  0 5������
�� .miscactvnull��� ��� null��  ��   E  F G F I  6 ;������
�� .aevtrappnull��� ��� null��  ��   G  H I H r   < I J K J c   < E L M L ^   < A N O N l  < ? P���� P \   < ? Q R Q o   < =���� 0 screenheight screenHeight R o   = >���� 0 	appheight 	appHeight��  ��   O m   ? @����  M m   A D��
�� 
long K o      ���� 0 yaxis yAxis I  S T S r   J W U V U c   J S W X W ^   J O Y Z Y l  J M [���� [ \   J M \ ] \ o   J K���� 0 screenwidth screenWidth ] o   K L���� 0 appwidth appWidth��  ��   Z m   M N����  X m   O R��
�� 
long V o      ���� 0 xaxis xAxis T  ^ _ ^ r   X ] ` a ` m   X Y����   a o      ���� 0 yaxis yAxis _  b c b r   ^ c d e d m   ^ _����   e o      ���� 0 xaxis xAxis c  f�� f r   d } g h g J   d v i i  j k j o   d g���� 0 xaxis xAxis k  l m l o   g j���� 0 yaxis yAxis m  n o n [   j o p q p o   j k���� 0 appwidth appWidth q o   k n���� 0 xaxis xAxis o  r�� r [   o t s t s o   o p���� 0 	appheight 	appHeight t o   p s���� 0 yaxis yAxis��   h l      u���� u n       v w v 1   z |��
�� 
pbnd w l  v z x���� x 4  v z�� y
�� 
cwin y m   x y���� ��  ��  ��  ��  ��   B 4   ) -�� z
�� 
capp z o   + ,���� 0 theapp theApp��  ��  ��       �� { |��   { ��
�� .aevtoappnull  �   � **** | �� }���� ~ ��
�� .aevtoappnull  �   � **** } k     ~ � �   � �   � �   � �   � �  - � �  5 � �  ?����  ��  ��   ~     ���������� *������������������������������ 0 theapp theApp��8�� 0 	appheight 	appHeight����� 0 appwidth appWidth
�� 
desk
�� 
cwin
�� 
pbnd�� $0 screenresolution screenResolution
�� 
cobj�� 0 screenwidth screenWidth�� �� 0 screenheight screenHeight
�� 
capp
�� .miscactvnull��� ��� null
�� .aevtrappnull��� ��� null
�� 
long�� 0 yaxis yAxis�� 0 xaxis xAxis�� �E�O�E�O�E�O� *�,�,�,E�UO��m/E�O���/E�O*��/ O*j O*j O��l!a &E` O��l!a &E` OjE` OjE` O_ _ �_ �_ �v*�k/�,FU ascr  ��ޭ