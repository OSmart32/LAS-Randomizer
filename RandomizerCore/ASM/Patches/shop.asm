; This contains the patches related to the shop


;* Always allow stealing
; Ignores sword check and checks shopkeeper direction
;settings stealing
.offset 0xa4a8f0
b 0xa4a910


;* Never allow stealing
; Ignores sword check and prevents the player from stealing
;settings !stealing
.offset 0xa4a8f0
b 0xa4a8f4


;* Set flags to check for stolen items
.offset 0xa4a9bc
nop
.offset 0xa4a9c0
nop
.offset 0xa4a9c4
nop
.offset 0xa4a9c8
nop
.offset 0xa4a9cc
mov w0, w8
.offset 0xa4a9d0
bl 0x8d2a70


;*Use the regular ShopItem datasheet even when the item is a Chamber Stone
.offset 0xa4a95c
nop
.offset 0xa4a960
b 0xa4a9ac
