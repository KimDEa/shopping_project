# 쇼핑몰 장바구니 & 할인 쿠폰 프로젝트

# 판매 상품 데이터
items_list = [
    ["무선 이어폰", 89_000, 3],
    ["텀블러", 15_000, 10],
    ["보조배터리", 32_000, 5],
    ["마우스패드", 9_000, 0],
    ["USB 허브", 18_000, 4]
]

class Items:
    def __init__(self, items_list):
        self.items_list = items_list
        self.cart = []
        self.total_discount = 0
        self.coupon_status = 0

    def menu(self):
        print("-"*57)
        print("1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
        print("-"*57)

        pick = input("원하시는 번호를 입력해주세요. : ")
        return int(pick)

    def pick_menu(self, pick):
        if pick == 1: # 상품목록
            print(f"\n===현재 메뉴: 1.상품 목록===")
            i.list(pick)

        if pick == 2: # 담기
            print(f"\n===현재 메뉴: 2.담기===")
            i.list(pick)
            i.add(pick)
            if self.coupon_status == 1:
                i.coupon()

        if pick == 3: # 빼기
            print(f"\n===현재 메뉴: 3.빼기===")
            #for k, index in enumerate(self.cart, start=1):
            #    print(f"{k}. 상품명: {index[0]}, 합계: {index[1]}, 수량: {index[2]}")
            i.subtract(pick)
            if self.coupon_status == 1:
                i.coupon()

        if pick == 4: # 장바구니
            if self.coupon_status == 1:
                i.coupon()
            i.shopping_cart()

        if pick == 5: # 쿠폰
            i.coupon()
            i.shopping_cart()
            

    def list(self, pick):
        for i, index in enumerate(self.items_list, start=1):
            if index[2] == 0:
                print(f"{i}. 제품: {index[0]}, 가격: {index[1]}, 수량: 품절")
            else:
                print(f"{i}. 제품: {index[0]}, 가격: {index[1]}, 수량: {index[2]}")

    def add(self, pick):
        add_item = int(input("\n담기 원하는 상품을 선택해 주세요.(0:뒤로) : "))
        if add_item == 0:
            back = i.menu()
            return back
        add_qty = int(input(f"\n선택한 상품: '{self.items_list[add_item - 1][0]}', 수량을 선택해 주세요. : "))
        if self.items_list[add_item - 1][2] < add_qty:
            print(f"\n현재 재고가 부족합니다. (담을수 있는 수량: {self.items_list[add_item - 1][2]}개.)")
            again = i.add(pick)
            pick = again
        else:
            print(f"\n{self.items_list[add_item - 1][0]}을/를 {add_qty}개 담았습니다.")
            self.items_list[add_item - 1][2] -= add_qty
            print(f"\n{self.items_list[add_item - 1][0]}의 현재 수량: {self.items_list[add_item - 1][2]}개.")

            prices = self.items_list[add_item - 1][1] * add_qty
            self.cart.append([self.items_list[add_item - 1][0], prices, add_qty])

    def subtract(self, pick):
        for k, index in enumerate(self.cart, start=1):
            print(f"{k}. 상품명: {index[0]}, 합계: {index[1]}, 수량: {index[2]}")
        
        sub_item = int(input("\n수정하기 원하는 상품을 선택해 주세요.(0:뒤로) : "))
        if sub_item == 0:
            back = i.menu()
            return back

        sub_pick = int(input(f"선택된 상품: {self.cart[sub_item - 1]}, 1.상품 삭제 / 2.수량 수정 : "))

        if sub_pick == 1:
            print(f"선택한 상품을 삭제했습니다. {self.cart.pop(sub_item - 1)}")
        elif sub_pick == 2:
            original_qty = self.cart[sub_item - 1][2]
            sub_num = int(input(f"선택한 상품: {self.cart[sub_item - 1]}, 원하는 수량을 입력해주세요. : "))
            self.cart[sub_item - 1][2] = sub_num
            self.cart[sub_item - 1][1] = (self.cart[sub_item - 1][1] / original_qty) * sub_num

            print(f"{self.cart[sub_item - 1][0]}의 수량을 {sub_num}으로 변경했습니다.")
            print(f"\n수정된 상품명: {self.cart[sub_item - 1][0]}, 수정된 가격: {self.cart[sub_item - 1][1]}, 수정된 수량: {self.cart[sub_item - 1][2]}")

    def shopping_cart(self):
        total_price = 0
        print(f"\n===현재 메뉴: 4.장바구니===")

        print("-"*58)
        for j, info in enumerate(self.cart, start=1):
            print(f"{j}. {info[0]},   x{info[2]}.             {info[1]}원")
            total_price += info[1]
        print("-"*58)
        print(f"상품 합계                                    {total_price}원\n")
        if self.total_discount > 0:
            print(f"할인                           -{self.total_discount}원 [{i.coupon_name}]\n")
        else:
            print(f"할인                            {self.total_discount}원\n")
        print(f"결제 금액              {total_price - self.total_discount}원")
        print("-"*58)


    def coupon(self):
        coupon_list = [
            "쿠폰 없음",
            "10% 할인 쿠폰(최대 5,000원 할인)",
            "3,000원 할인 쿠폰(20,000원 이상 구매 시)"
        ]
        total_price = 0
        discount = 0

        if self.coupon_status == 0:
            print(
                "(1).쿠폰 없음\n",
                "(2).10% 할인 쿠폰 (최대 5,000원)\n",
                "(3).3,000원 할인 쿠폰 (20,000원 이상 구매 시)"
            )

            discount = int(input("할인 쿠폰을 선택해 주세요.[ (1)쿠폰 없음 / (2)10% 할인 / (3)3,000원 할인 ] : "))

        discount = discount

        if discount == 2:
            for i in self.cart:
                total_price += i[1]
            #total_price_coupon = total_price * 0.9
            self.total_discount = total_price * 0.1
            if self.total_discount > 5_000:
                self.total_discount = 5_000
        if discount == 3:
            for i in self.cart:
                total_price += i[1]
            if total_price >= 20_000:
                self.total_discount = 3_000
            
        self.coupon_name = coupon_list[discount - 1]
        self.coupon_status = 1
        self.coupon_name

    def pay(self):
        pass
        

if __name__ == "__main__":
    i = Items(items_list)
    while True:
        pick =i.menu()
        if pick == "q":
            print("서비스를 종료합니다.")
            break
        else:
            i.pick_menu(pick)