from PIL import Image
def chuyendoi_img2pdf(files):
	pdf1_filename = "/Users/apple/Desktop/bbd1.pdf"
	files[0].save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=files)