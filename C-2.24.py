#Misalkan Anda berada di tim desain untuk pembaca e-book baru.
#Apa kelas dan metode utama yang dibutuhkan perangkat lunak Python untuk pembaca Anda?
#Anda harus menyertakan diagram pewarisan untuk kode ini, tetapi Anda tidak perlu menulis kode yang sebenarnya.
#Arsitektur perangkat lunak Anda setidaknya harus menyertakan cara bagi pelanggan untuk membeli buku baru, melihat daftar buku yang mereka beli, dan membaca buku yang mereka beli.

#Book class --> get_price(), get_id(), get_author(), num_of_pages(), get_summary()
#	Book(title, author, price, unique_id, summary, pages)
#Nested in Book will be a Page class --> read_text(), highlight_chars(seq_of_chars), 
#get_page_number(), next_page(), go_to_page(n)
#	Page(page_number, text)
#Customer Class --> get_account_info(), see_shelf(), read_book(title), buy_book(title)
#	Customer(account_info, shelf)
