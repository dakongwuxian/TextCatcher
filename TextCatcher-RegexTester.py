"""
版权所有 (c) 2025 [吴宪]

本软件TermPlus（以下简称“软件”）为个人非商业用途开源发布。任何人均可免费使用、复制、修改和分发本软件，但仅限于个人非商业用途。
对于商业用途（包括但不限于嵌入商业产品、提供商业服务、营利分发等），必须事先获得作者的书面许可。

本软件按“现状”提供，不附带任何明示或暗示的担保，包括但不限于对适销性、特定用途适用性以及不侵权的保证。
在任何情况下，作者均不对因使用或无法使用本软件而产生的任何直接、间接、偶然、特殊或后续损害承担责任。

如需商业授权或有任何疑问，请联系：[dakongwuxian@gmail.com]
"""
import base64
import io
from io import BytesIO
from PIL import Image, ImageTk
from pydoc import text
import tkinter as tk
from tkinter import ttk,filedialog,messagebox
import tkinter.filedialog as fd
import tkinter.messagebox as messagebox
import tkinter.messagebox as mb
import re
import time
import webbrowser

# 嵌入的二维码 base64 字符串（PNG 格式）
img_base64 = (
"iVBORw0KGgoAAAANSUhEUgAAANgAAADZAQAAAABqB8PlAAAAGmVYSWZNTQAqAAAACAABARIAAwAA"
"AAEAAQAAAAAAABPAdecAAATCSURBVHjazVjbjuNEED3ltmgLJDp8wKS9/+EdZzV8CJ+wvGWkRenR"
"rJR5Wz6FD1iYzmSl5SMQsmd546WNBOqA7cNDkrlkLwybGOG3uNLlrqpT51S3EO99Evy3NgQARVnT"
"hKjPPaQyJsxiAcAOs5cZW3V5jDDS7hnK7rhpjGQo2Q8U+0ocrphLkPgjFsmbipg5dJIjAeC3f3wJ"
"AKMD5bqsK4yeXnQTYWdFMuV31l3c/kwPWdt+HcPk1nOXdEmwxq1A+6YHgG44nGl6MLeoV07RS49m"
"dOagWA3yPQkjoMC1BETXTjCGAS5S/+oGu7ur2/16hSS56EFgquilN8bMSZIcJp8e+AlI3HdIZzgr"
"u2/TP7QDPCrQAcqPrQnQDqoSBkxRetvv0bfuPpbWPDXZ8MSMHpYBdMpjDMOg2ar6sLFnN7bpSk48"
"AGS6haoZREe89keSD8KDdFAeAIOmU156Q8wcynqo2k716mRBjoAzfv/EX6+J4/lRsrsuyQ+rARk8"
"+p3Yp+WmtlF5jAFCz71if2ANaDe8pLE46RUMRa9SVQPCi9VE1bkdprZ0Jb3QBLJVHpaEdkVhh6kt"
"YpyikB4E2UJIGzBVy2Xd2zRe3HfDsLcGIGieL1kZBmB2vqxsMJyzBSyTTQOP7rTyobAUAMD73XlC"
"t0XZA8AUUKwZwoz0Uj20tjIn2/fYPtnliRSz7LU/EY7COsRRY4Nkv0+sVHfWjf4xvuzBuZ57lBXC"
"Wg0YDQOmherHA2E3ovSqZjB2/T3hC9KXvd1g924r84bBD7CXu2LgN3uZAlJXwaxj74EwBTA+4Kwo"
"93Idyxa2Ctw8IRiHsh2obxPjLrqJXGHUrCmXdtREdJN6GM1JACh/9PjYmPWLvwLxIipvt7Nwfi8d"
"+2NpHoFjABss9RaYTgH7rt4MB4jPbfHptvgEUiAHkmaVqeVzocFXAIA/fzPM1HLphzrnaFeUi8pu"
"+7Y3IUCzfTgv/ctc6znbkhXClidM0BGKNXfmrA/7jA/VHB0BVVkas+0VzF7HouxtEm944o43n6La"
"9flqkTw49uztl65FAiDFU5SeuTRYneovcZT0QnQni+vrj69ttqtet4KWaJl/8/hJvQCgU5RXRwLJ"
"tAPzQbCUNhEn885eh4DVZ233qDJmNP1aVEsMNJvOWkhvA01EyWq8ns/K+h524wE1Z6q4qCsTNM9Z"
"2R7ALELxrV6pDsODMb2j0nkuuFW2gFlbLnrQ6KiWJGkwhfIy0OzGOZckKwPSFaoXGsMIVQ1zH5IC"
"6B6ryxxmlal2kY+b2q5cgbIqB8KSpsf4c8N5LJSXygQz53J5p7ZfAG632fbRgD6Da/ESeNnjDPgU"
"z371P/hNbQupqwA9d1A9DAMASM19eOKD5/dWKpBxds4lKxjoeJB54p063YjI5Hg8bkRneNXJI4IO"
"3eS6HuYMG2Zsi7KXEABFLwwh4v68xHdIy8djdyXPwBy21vFMpBODBlik46S/d7e242a/2H9+25Bv"
"bb+8qZpRc9qq1aMKAdqV9ONDcXKy27eA9HUwWeyeP7k6aiRc0L8qFvkwPKHZTY6v7ahuXLoErgFj"
"vhZIN9Bd3pmk6tLmAVitTk+Px8ZIRFFeJu9fl+9xl/c/uhP/kO1vBYeg5BFXBCUAAAAASUVORK5C"
"YII="
)

class MainGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Text Cather - Regex Tester")
        self.geometry("1200x800")

        style = ttk.Style()
        # 定义一个名为 'Border.TFrame' 的新样式
        style.configure('Border.TFrame', 
                        relief="solid",         # 设置扁平边框，也可以是 'raised' 等
                        borderwidth=1,          # 设置边框宽度
                        background="lightgray"  # 确保背景颜色与边框区分开
                       )

        # 创建菜单栏
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # About 菜单
        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.about_menu.add_command(label="Developed by Xian.Wu", state="disabled")
        self.about_menu.add_command(label="dakongwuxian@gmail.com", state="disabled")

        self.about_menu.add_command(label="Ver. 20251209", state="disabled")

        self.about_menu.add_command(label="Donation Here.",command=self.show_about_window,state="normal")


        # 用于存储所有动态生成的控件引用
        #self.dynamic_widgets = []

        # 初始化所有动态创建和删除的控件变量为 None
        #self.acsii_unicode_class_label = None
        #self.acsii_unicode_class_entry = None

        # 用于处理input text中的文本的信息
        self.input_string_content = None
        self.input_text_selected_match_string=[]
        self.match_string_start_index=[]
        self.match_string_end_index=[]
        self.match_string_regular_expression=[]
        self.highlight_items = []


        # 主框架
        self.main_frame = ttk.Frame(self, padding=10)
        self.main_frame.pack(fill="both", expand=True)

        # 2列均分
        self.main_frame.columnconfigure(0, weight=1, uniform="col")
        self.main_frame.columnconfigure(1, weight=1, uniform="col")
        #main_frame.columnconfigure(2, weight=1, uniform="col")

        self.main_frame.rowconfigure(0, weight=0)
        #self.main_frame.rowconfigure(0, minsize=100)
        self.main_frame.rowconfigure(1, weight=1)

        # 上方frame ————————————————————————————————————————————————————————————————————————————————————

        self.up_frame = ttk.Frame(self.main_frame) #, style='Border.TFrame'
        self.up_frame.grid(row=0, column=0,sticky="nsew", padx=5,columnspan=2)
        # 让 up_frame 的列的权重为1, 才能实现后面的sticky ew的自动占满
        self.up_frame.columnconfigure(0, weight=1)

        self.up_frame.rowconfigure(0,weight=0)
        self.up_frame.rowconfigure(1,weight=0)

        # self.up_frame.rowconfigure(1,weight=0)
        # self.up_frame.rowconfigure(2,weight=1)
        # self.up_frame.rowconfigure(3,weight=0)

        self.regular_expression_area_label = ttk.Label(self.up_frame, text="Regular Expression",font=("微软雅黑", 11,"bold"))
        self.regular_expression_area_label.grid(row=0,column=0,sticky="w", pady=5)

        self.up_button_frame = ttk.Frame(self.up_frame) #, style='Border.TFrame'
        self.up_button_frame.grid(row=1, column=0,sticky="ew", padx=5)
        self.up_button_frame.columnconfigure(4, weight=1)


        self.load_regex_button = ttk.Button(self.up_button_frame,text="Load Regex from File",command=lambda: self.load_regex_button_function())
        self.load_regex_button.grid(row=0,column=0,sticky="w",padx=5)
        self.save_regex_button = ttk.Button(self.up_button_frame,text="Save Regex as File",command=lambda: self.save_regex_button_function())
        self.save_regex_button.grid(row=0,column=1,sticky="w",padx=5)
        self.focus_to_last_regex_button = ttk.Button(self.up_button_frame,text="↑",command=lambda: self.focus_to_last_regex_button_function())
        self.focus_to_last_regex_button.grid(row=0,column=2,sticky="w",padx=5)
        self.focus_to_next_regex_button = ttk.Button(self.up_button_frame,text="↓",command=lambda: self.focus_to_next_regex_button_function())
        self.focus_to_next_regex_button.grid(row=0,column=3,sticky="w",padx=5)

        self.show_regex_table_button = ttk.Button(self.up_button_frame,text="Common Regex",command=lambda: self.show_regex_table_function())
        self.show_regex_table_button.grid(row=0,column=5,sticky="e",padx=5)
        self.open_regex_tutorial_button = ttk.Button(self.up_button_frame,text="Regex Tutorial",command=lambda: self.open_regex_tutorial_function())
        self.open_regex_tutorial_button.grid(row=0,column=6,sticky="e",padx=5)

        # 用多行文本框显示多个正则表达式
        # ====== 多行文本框区域 ======
        self.up_text_frame = ttk.Frame(self.up_frame)
        self.up_text_frame.grid(row=2, column=0,sticky="ew",pady=10)
        self.regex_text_scrollbar = ttk.Scrollbar(self.up_text_frame)
        self.regex_text_scrollbar.pack(side="right", fill="y")
        
        self.regex_text_input = tk.Text(self.up_text_frame,wrap="word",yscrollcommand=self.regex_text_scrollbar.set,font=("Consolas", 10),height=10)
        self.regex_text_input.pack(fill="both", expand=True)
        self.regex_text_scrollbar.config(command=self.regex_text_input.yview)
        # 设置捕获组高亮的tag
        self.regex_text_input.tag_configure("capture_group", foreground="#cc6600")
        # 自动高亮捕获组
        self.regex_text_input.bind("<KeyRelease>", lambda e: self.highlight_capture_groups())
        # 绑定到 Text
        self.regex_text_input.bind("<KeyRelease>", self.update_highlight_items)

        #self.regex_entry_notebook = ttk.Notebook(self.up_text_frame,)# 本身使用默认样式 'TNotebook' :contentReference[oaicite:5]{index=5}


        # 左侧frame ————————————————————————————————————————————————————————————————————————————

        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.grid(row=1, column=0, sticky="nsew", padx=5)

        # ====== 标题 ======
        self.left_title_label = ttk.Label(self.left_frame, text="Input Text Area", font=("微软雅黑", 11, "bold"))
        self.left_title_label.pack(anchor="w", pady=5)
        # ====== 按钮区域 ======
        self.left_btn_frame = ttk.Frame(self.left_frame)
        self.left_btn_frame.pack(fill="x", pady=5)
        self.open_file_button = ttk.Button(self.left_btn_frame,text="Open File",command=lambda: self.open_file_button_function())
        self.open_file_button.grid(row=0,column=0,sticky="w",padx=5)

        style = ttk.Style()
        style.configure("Match.TButton",
                        foreground="#1a5f99")  # 按钮文字颜色
        style.map("Match.TButton",
                  foreground=[("active", "#1a5f99")])# 鼠标悬停颜色

        self.mark_as_mark_button = ttk.Button(self.left_btn_frame,style="Match.TButton",text="Set as Match",command=lambda: self.mark_as_mark_button_function())
        self.mark_as_mark_button.grid(row=0,column=1,sticky="w",padx=5)

        style = ttk.Style()
        style.configure("Target.TButton",
                        foreground="#cc6600")   # 按钮文字颜色
        style.map("Target.TButton",
                  foreground=[("active", "#cc6600")])# 鼠标悬停颜色

        self.mark_as_target_button = ttk.Button(self.left_btn_frame,style="Target.TButton",text="Set as Capture",command=lambda: self.mark_as_target_button_function())
        self.mark_as_target_button.grid(row=0,column=2,sticky="w",padx=5)

        style = ttk.Style()
        style.configure("NotCare.TButton",
                        foreground="#666666")   # 按钮文字颜色
        style.map("Target.TButton",
                  foreground=[("active", "#666666")])# 鼠标悬停颜色

        self.mark_as_not_care_button = ttk.Button(self.left_btn_frame,style="NotCare.TButton",text="Set as Not Care",command=lambda: self.mark_as_not_care_button_function())
        self.mark_as_not_care_button.grid(row=0,column=3,sticky="w",padx=5)
        self.unmark_button = ttk.Button(self.left_btn_frame,text="Unmark",command=lambda: self.unmark_button_function())
        self.unmark_button.grid(row=0,column=4,sticky="w",padx=5)

        # ====== 多行文本框区域 ======
        self.left_text_frame = ttk.Frame(self.left_frame)
        self.left_text_frame.pack(fill="both", expand=True)
        self.left_scrollbar = ttk.Scrollbar(self.left_text_frame)
        self.left_scrollbar.pack(side="right", fill="y")
        self.left_v_scrollbar = ttk.Scrollbar(self.left_text_frame,orient="horizontal")
        self.left_v_scrollbar.pack(side="bottom", fill="x")

        self.left_text_widget = tk.Text(self.left_text_frame,wrap="none",yscrollcommand=self.left_scrollbar.set,xscrollcommand=self.left_v_scrollbar.set,font=("Consolas", 10))
        self.left_text_widget.pack(fill="both", expand=True)
        self.left_scrollbar.config(command=self.left_text_widget.yview)
        self.left_v_scrollbar.config(command=self.left_text_widget.xview)

        self.bind_text_sync_dynamic()
        self.bind_cursor_highlight_sync()

        # 右侧frame ——————————————————————————————————————————————————————————————————————————————————

        self.right_frame =  ttk.Frame(self.main_frame)
        self.right_frame.grid(row=1, column=1, sticky="nsew", padx=5)


        self.right_title_label = ttk.Label(self.right_frame, text="Capture Data Area", font=("微软雅黑", 11, "bold"))
        self.right_title_label.pack(anchor="w", pady=5)

        self.right_btn_frame = ttk.Frame(self.right_frame)
        self.right_btn_frame.pack(fill="x", pady=5)

        self.run_button = ttk.Button(self.right_btn_frame,text="Run",command=lambda: self.run_button_function())
        self.run_button.grid(row=0,column=0,sticky="w",padx=5)
        self.save_as_button = ttk.Button(self.right_btn_frame,text="Save as..",command=lambda: self.save_as_button_function())
        self.save_as_button.grid(row=0,column=3,sticky="w",padx=5)

        self.match_mode_value = tk.IntVar(value=0)
        self.match_mode_checkbutton = ttk.Checkbutton(self.right_btn_frame,text="Match in Sequence",variable=self.match_mode_value)
        self.match_mode_checkbutton.grid(row=0,column=1,sticky="w",padx=5)

        self.show_row_number_value = tk.IntVar(value=0)
        self.show_row_number_checkbutton = ttk.Checkbutton(self.right_btn_frame,text="Capture Row Num",variable=self.show_row_number_value)
        self.show_row_number_checkbutton.grid(row=0,column=2,sticky="w",padx=5)


        self.right_text_frame = ttk.Frame(self.right_frame)
        self.right_text_frame.pack(fill="both", expand=True)

        self.right_scrollbar = ttk.Scrollbar(self.right_text_frame)
        self.right_scrollbar.pack(side="right", fill="y")

        self.right_v_scrollbar = ttk.Scrollbar(self.right_text_frame,orient="horizontal")
        self.right_v_scrollbar.pack(side="bottom", fill="x")

        self.right_text_widget = tk.Text(self.right_text_frame,wrap="none",yscrollcommand=self.right_scrollbar.set,xscrollcommand=self.right_v_scrollbar.set,font=("Consolas", 10))
        self.right_text_widget.pack(fill="both", expand=True)
        self.right_scrollbar.config(command=self.right_text_widget.yview)
        self.right_v_scrollbar.config(command=self.right_text_widget.xview)

    def create_new_tab(self):
        new_title = f"{len([t for t in self.notebook.tabs() if self.notebook.tab(t, 'text') != '']) + 1}"
        self.add_tab(new_title)
        self.notebook.select(self.notebook.tabs()[-1])

    def delete_current_tab(self):
        current = self.notebook.select()
        if current:
            self.notebook.forget(current)

    def button_action(self, btn_name):
        """
        按钮占位函数
        """
        print(f"Button pressed: {btn_name}")

    def on_main_type_change(self, event):
        #"""一级菜单改变时的分发逻辑"""
        # 第一步：先清场
        self.clear_dynamic_widgets()
        selection = self.node_type_var.get()

        if selection == "Fixed String":
            self.setup_fixed_string_ui()
        elif selection == "Character Class":
            self.setup_charactor_class_ui()
        elif selection == "Character Range":
            self.setup_character_range_ui()
        elif selection == "Word Boundary Assertion":
            self.setup_boundary_ui()
        elif selection == "Back Reference":
            self.setup_backref_ui()

    def clear_dynamic_widgets(self):
        # """销毁列表中的所有控件，并清空列表"""
        for widget in self.dynamic_widgets:
            if widget.winfo_exists(): # 安全起见，检查控件是否还存在
                widget.destroy()
        self.dynamic_widgets.clear() # 清空列表

    # ==========================================
    # 1. Fixed String UI
    # ==========================================
    def setup_fixed_string_ui(self):
        self.type_edit_second_level_label.config(text="String:")
        self.setup_fixed_string_ui_entry = ttk.Entry(self.mid_btn_frame)
        self.setup_fixed_string_ui_entry.grid(row=1, column=9, sticky="ew", padx=5, pady=5)

        # 【关键】加入管理列表
        self.dynamic_widgets.append(self.setup_fixed_string_ui_entry)
        #setup_fixed_string_ui_entry.insert(0, "abc") # 示例

    # ==========================================
    # 2. Predefined Character Class UI (\d, \w, \xhh...)
    # ==========================================
    def setup_charactor_class_ui(self):
        self.type_edit_second_level_label.config(text="Class:")

        self.setup_charactor_class_ui_combobox_var = tk.StringVar()
        self.setup_charactor_class_ui_combobox = ttk.Combobox(self.mid_btn_frame, textvariable=self.setup_charactor_class_ui_combobox_var, state="readonly")
        self.setup_charactor_class_ui_combobox.grid(row=1, column=9, sticky="w", padx=5, pady=5)

        # 【关键】加入管理列表
        self.dynamic_widgets.append(self.setup_charactor_class_ui_combobox)
        
        # 这里只放预定义字符和转义符
        options = [
            r"\d (Digit)", r"\D (Non-digit)", 
            r"\w (Word char)", r"\W (Non-word)", 
            r"\s (Whitespace)", r"\S (Non-whitespace)",
            r". (Any char)",
            r"\t (Tab)", r"\r (CR)", r"\n (LF)",
            r"\xhh (Hex Value)", r"\uhhhh (Unicode)"
        ]
        self.setup_charactor_class_ui_combobox['values'] = options
        self.setup_charactor_class_ui_combobox.current(0)

        
        # 绑定事件，处理 Hex/Unicode 需要额外输入框的情况
        self.setup_charactor_class_ui_combobox.bind("<<ComboboxSelected>>", self.when_charactor_class_change)

    def when_charactor_class_change(self, event):
        # 检查label和entry是否存在，如果存在，先删除
        # 检查变量是否已被赋值 (不为 None)
        if self.acsii_unicode_class_label is not None:
            self.acsii_unicode_class_label.destroy()
            self.acsii_unicode_class_label = None  # 销毁后重置，为下次检查做准备
        
        if self.acsii_unicode_class_entry is not None:
            self.acsii_unicode_class_entry.destroy()
            self.acsii_unicode_class_entry = None # 销毁后重置

        
        val = self.setup_charactor_class_ui_combobox_var.get()
        if "xhh" in val or "uhhhh" in val:
            self.acsii_unicode_class_label = ttk.Label(self.mid_btn_frame, text="Value:", font=("微软雅黑", 9))
            self.acsii_unicode_class_label.grid(row=2, column=8, sticky="e", padx=5, pady=5)

            self.acsii_unicode_class_entry = ttk.Entry(self.mid_btn_frame)
            self.acsii_unicode_class_entry.grid(row=2, column=9, sticky="ew", padx=5, pady=5)
            self.acsii_unicode_class_entry.insert(0, r"\x00" if "xhh" in val else r"\u0000")

            # 加入动态管理列表
            self.dynamic_widgets.append(self.acsii_unicode_class_label)
            self.dynamic_widgets.append(self.acsii_unicode_class_entry)
            


    # ==========================================
    # 3. Character Range UI ([a-z])
    # ==========================================
    def setup_character_range_ui(self):

        self.type_edit_second_level_label.config(text="Range:")
        
        # Range 输入
        # min entry
        self.range_min_entry = ttk.Entry(self.mid_btn_frame,width=4)
        self.range_min_entry.grid(row=1, column=9, sticky="ew", padx=5, pady=5)
        # 横杠 slash
        self.range_slash_label = ttk.Label(self.mid_btn_frame, text="-")
        self.range_slash_label.grid(row=1, column=10, sticky="ew", padx=5, pady=5)
        # max entry
        self.range_max_entry = ttk.Entry(self.mid_btn_frame,width=4)
        self.range_max_entry.grid(row=1, column=11, sticky="ew", padx=5, pady=5)
        self.range_min_entry.insert(0, "a")
        self.range_max_entry.insert(0, "z")
        # 取反 check button
        self.character_range_negate_checkbutton_var = tk.BooleanVar(value=False)
        self.character_range_negate_checkbutton = ttk.Checkbutton(self.mid_btn_frame,variable=self.character_range_negate_checkbutton_var,text="Negate (^)")
        self.character_range_negate_checkbutton.grid(row=2, column=9,columnspan=3, sticky="w", padx=5, pady=5)

        # 加入动态管理列表
        self.dynamic_widgets.append(self.range_min_entry)
        self.dynamic_widgets.append(self.range_slash_label)
        self.dynamic_widgets.append(self.range_max_entry)
        self.dynamic_widgets.append(self.character_range_negate_checkbutton)





    # ==========================================
    # 4. Word Boundary UI (\b)
    # ==========================================
    def setup_boundary_ui(self):
        self.type_edit_second_level_label.config(text="")
        
        # 取反 check button
        self.setup_boundary_checkbutton_var = tk.BooleanVar(value=False)
        self.setup_boundary_checkbutton = ttk.Checkbutton(self.mid_btn_frame,variable=self.character_range_negate_checkbutton_var,text="Negate (^)")
        self.setup_boundary_checkbutton.grid(row=1, column=9, sticky="w", padx=5, pady=5)

        # 加入动态管理列表
        self.dynamic_widgets.append(self.setup_boundary_checkbutton)

    # ==========================================
    # 5. Back Reference UI (\1)
    # ==========================================
    def setup_backref_ui(self):
        self.type_edit_second_level_label.config(text="Back Ref.:")
        
        self.setup_backref_combobox_var = tk.StringVar()
        self.setup_backref_combobox = ttk.Combobox(self.mid_btn_frame, textvariable=self.setup_backref_combobox_var, state="readonly")
        
        # 【修正】这里将类别提升到一级菜单
        self.setup_backref_combobox['values'] = (
            "Group #1", 
            "Group #2",
            "Group #3",
            "Group #4",
            "Group #5",
            "Group #6",
            "Group #7",
            "Group #8",
            "Group #9",
            "Group #10"
        )
        self.setup_backref_combobox.grid(row=1, column=9, sticky="ew", padx=5, pady=5)
        #self.setup_backref_combobox.bind("<<ComboboxSelected>>", self.on_setup_backref_combobox)

        # 加入动态管理列表
        self.dynamic_widgets.append(self.setup_backref_combobox)


    def open_file_button_function(self):
        # 打开文件浏览器，选择txt文件
        file_path = filedialog.askopenfilename(
            title="Open TXT File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        # 如果用户取消选择，直接返回
        if not file_path:
            return

        try:
            # 读取文件内容
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # --- 清空已有内容和高亮 ---
            self.left_text_widget.delete("1.0", tk.END)
        
            if hasattr(self, "highlight_items"):
                for item in self.highlight_items:
                    tag = item.get("tag")
                    if tag:
                        try:
                            self.left_text_widget.tag_remove(tag, "1.0", tk.END)
                            self.left_text_widget.tag_delete(tag)
                        except Exception:
                            pass
                self.highlight_items.clear()
            # --- 清空完成 ---
            # 插入新内容
            self.left_text_widget.insert(tk.END, content)

            self.input_string_content = content

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file:\n{e}")

    def mark_as_mark_button_function(self):
        # 确保 highlight_items 存在
        if not hasattr(self, "highlight_items"):
            self.highlight_items = []

        try:
            sel_start = self.left_text_widget.index("sel.first")
            sel_end   = self.left_text_widget.index("sel.last")
        except:
            messagebox.showerror("Error", "Select text first!")
            return

        selected_text = self.left_text_widget.get(sel_start, sel_end)

        # ------------------------------
        # 不再生成随机 tag，改为统一用 apply_segment_tags
        # ------------------------------
        new_item = {
            "start": sel_start,
            "end": sel_end,
            "text": selected_text,
            "segments": [{
                "text": selected_text,
                "type": "match"
            }],
        }

        # 使用统一 tag 管理函数
        self.apply_segment_tags(new_item)

        # 添加到列表
        self.highlight_items.append(new_item)

        # 生成 regex
        regex_text = self.build_regex_from_segments(new_item)
        new_item["regex"] = regex_text

        self.regex_text_input.delete("1.0", tk.END)
        self.regex_text_input.insert("1.0", regex_text)

        self.left_text_widget.tag_remove("sel", "1.0", "end")
        self.left_text_widget.update_idletasks()

    def build_regex_from_segments(self, item):
        parts = []
        for seg in item["segments"]:
            t = seg["text"]
            tp = seg["type"]

            if tp == "match":
                parts.append(self.translate_to_regex(t))

            elif tp == "capture":
                parts.append("(" + self.generalize_regex_pattern(t) + ")")

            elif tp == "notcare":
                parts.append(r"[\s\S]*?")

        return "".join(parts)

    def apply_segment_tags(self, item):
        """
        为 item 的所有 segments 应用 tag。
        如果 item 没有 tag，则自动创建一个新的 tag 基名。
        """

        # 1) 如果没有 tag，就自动生成一个
        if "tag" not in item or not item["tag"]:
            base_tag = f"seg_{id(item)}"
            item["tag"] = base_tag
        else:
            base_tag = item["tag"]

        # 2) 删除旧 tag
        #   注意：不能假设每个 tag_names 都以 base_tag 开头，要安全判断
        for tag in list(self.left_text_widget.tag_names()):
            if tag.startswith(base_tag):
                self.left_text_widget.tag_delete(tag)

        hl_start = item["start"]
        pos = 0
        base_tag = item["tag"]

        for i, seg in enumerate(item["segments"]):
            seg_tag = f"{base_tag}_{i}"

            if seg["type"] == "match":
                self.left_text_widget.tag_configure(seg_tag, background="#cce8ff", foreground="black",selectforeground="gray", selectbackground="white")
            elif seg["type"] == "capture":
                self.left_text_widget.tag_configure(seg_tag, background="#cce8ff", foreground="#cc6600",selectforeground="gray", selectbackground="#cc6600")
            elif seg["type"] == "notcare":
                self.left_text_widget.tag_configure(seg_tag, background="light gray", foreground="white",selectforeground="black", selectbackground="white")

            seg_len = len(seg["text"])
            seg_start = self.left_text_widget.index(f"{hl_start}+{pos}c")
            seg_end   = self.left_text_widget.index(f"{hl_start}+{pos+seg_len}c")

            self.left_text_widget.tag_add(seg_tag, seg_start, seg_end)
            pos += seg_len
        
        self.left_text_widget.update_idletasks()

    def translate_to_regex(self, text: str) -> str:
        result = []
        i = 0
        length = len(text)

        while i < length:
            ch = text[i]

            # 1️⃣ 数字 → 转成 \d{N}，修改，不转化数字
            if ch.isdigit():
                j = i
                while j < length and text[j].isdigit():
                    j += 1
                num_len = j - i
                #result.append(r"\d{" + str(num_len) + "}")
                result.append(text[i:j])
                i = j
                continue

            # 2️⃣ 空白字符（空格 / Tab）→ \s{N}
            if ch.isspace():
                j = i
                while j < length and text[j].isspace():
                    j += 1
                space_len = j - i
                result.append(r"\s{" + str(space_len) + "}")
                i = j
                continue

            # 3️⃣ 字母和中文 → 保留原样
            if ch.isalpha() or '\u4e00' <= ch <= '\u9fff':
                result.append(ch)
                i += 1
                continue

            # 4️⃣ 其他字符 → 正则特殊字符需要转义
            if ch in r".^$*+?{}[]\|()":
                result.append("\\" + ch)
            else:
                result.append(ch)

            i += 1

        return "".join(result)

    # 在input text 文本框绑定修改函数，文本被修改后更新相关变量
    def bind_text_sync_dynamic(self):
        self.left_text_widget.edit_modified(False)
        self.left_text_widget.bind("<<Modified>>", self.on_text_modified_dynamic)

    def on_text_modified_dynamic(self, event=None):
        """
        动态同步 self.highlight_items 逻辑：
        - 如果文本被全部删除或被替换（长度变化大于原长度），则清空 highlight_items
        - 否则保留已有高亮，不更新 start/end/text
        """
        # 清除 Text 的修改标志
        self.left_text_widget.edit_modified(False)

        # 获取当前文本
        current_text = self.left_text_widget.get("1.0", tk.END)

        # 判断是否为整体清空或大幅修改
        if not hasattr(self, "last_text_content"):
            self.last_text_content = current_text

        if len(current_text) == 1 or len(current_text) < len(self.last_text_content) // 2:
            # 整体清空或大幅替换 -> 删除所有 highlight
            if hasattr(self, "highlight_items"):
                for item in self.highlight_items:
                    tag = item.get("tag")
                    if tag:
                        self.left_text_widget.tag_remove(tag, "1.0", tk.END)
                        try:
                            self.left_text_widget.tag_delete(tag)
                        except Exception:
                            pass
                self.highlight_items.clear()

        # 更新 last_text_content
        self.last_text_content = current_text

    def bind_cursor_highlight_sync(self):
        # 键盘移动光标
        #self.left_text_widget.bind("<KeyRelease>", self.on_cursor_move_highlight)
        # 鼠标点击移动光标
        self.left_text_widget.bind("<ButtonRelease>", self.on_cursor_move_highlight)

    def on_cursor_move_highlight(self, event=None):
        # 获取光标当前索引
        cursor_index = self.left_text_widget.index(tk.INSERT)

        for item in getattr(self, "highlight_items", []):
            start = item.get("start")
            end = item.get("end")

            if start is None or end is None:
                continue  # 如果没有 start/end，就跳过

            # 判断光标是否在该段范围内
            if self.left_text_widget.compare(cursor_index, ">=", start) and \
               self.left_text_widget.compare(cursor_index, "<=", end):
                # 更新 regex_text_input 为该高亮对应 regex
                self.regex_text_input.delete("1.0", tk.END)
                self.regex_text_input.insert("1.0", item.get("regex", ""))
                self.highlight_capture_groups()
                return  # 找到后直接退出
        # 光标不在任何高亮段，则清空 regex_text_input 或保持原样
        # self.regex_text_input.delete(0, tk.END)

    def mark_as_target_button_function(self):
        try:
            sel_start = self.left_text_widget.index("sel.first")
            sel_end   = self.left_text_widget.index("sel.last")
        except:
            messagebox.showerror("Error", "Select text first！")
            return

        # 找所属 highlight_item
        item = None
        for it in self.highlight_items:
            if (self.left_text_widget.compare(sel_start, ">=", it["start"]) and
                self.left_text_widget.compare(sel_end, "<=", it["end"])):
                item = it
                break

        if item is None:
            messagebox.showerror("Error", "Select is not within Match section!")
            return

        # 第一次创建 segments
        if "segments" not in item:
            item["segments"] = [{
                "text": item["text"],
                "type": "match"
            }]

        # 1. 切分 segments
        self.split_segments(item, sel_start, sel_end)

        # 2. 给选中的段赋 type="capture"
        for seg in item["segments"]:
            if seg["type"] is None:
                seg["type"] = "capture"

        # 3. 重新生成 regex
        item["regex"] = self.build_regex_from_segments(item)

        # 4. 刷新 UI 高亮
        self.apply_segment_tags(item)

        # 更新右侧文本
        self.regex_text_input.delete("1.0", tk.END)
        self.regex_text_input.insert("1.0", item["regex"])

        self.highlight_capture_groups()

    def mark_as_not_care_button_function(self):
        try:
            sel_start = self.left_text_widget.index("sel.first")
            sel_end   = self.left_text_widget.index("sel.last")
        except Exception:
            messagebox.showerror("Error", "Select text first！")
            return

        # 找 highlight_item
        item = None
        for it in self.highlight_items:
            if (self.left_text_widget.compare(sel_start, ">=", it["start"]) and
                self.left_text_widget.compare(sel_end, "<=", it["end"])):
                item = it
                break

        if item is None:
            messagebox.showerror("Error", "Select is not within Match section!")
            return

        # 确保 segments 存在
        if "segments" not in item or not item["segments"]:
            item["segments"] = [{"text": item["text"], "type": "match"}]

        # 切分段，使选区对齐 segment
        self.split_segments(item, sel_start, sel_end)

        # 计算选区在 highlight_item 内的字符偏移
        try:
            sel_rel_start = self.left_text_widget.count(item['start'], sel_start, "chars")[0]
            sel_rel_end   = self.left_text_widget.count(item['start'], sel_end, "chars")[0]
        except Exception:
            # fallback：选区相对偏移全段
            sel_rel_start = 0
            sel_rel_end = sum(len(s["text"]) for s in item["segments"])

        # 遍历 segments，只修改与选区有重叠的段
        pos = 0
        for seg in item["segments"]:
            seg_start = pos
            seg_end   = pos + len(seg["text"])
            if seg_end > sel_rel_start and seg_start < sel_rel_end:
                seg["type"] = "notcare"
            pos += len(seg["text"])

        # 合并连续相同 type 的段，防止过多 segment
        merged = []
        for s in item["segments"]:
            if merged and merged[-1]["type"] == s["type"]:
                merged[-1]["text"] += s["text"]
            else:
                merged.append({"text": s["text"], "type": s["type"]})
        item["segments"] = merged

        # 重建 regex
        try:
            item["regex"] = self.build_regex_from_segments(item)
        except Exception:
            # fallback 简单拼接
            item["regex"] = "".join(
                ("(.*)" if s["type"]=="notcare" else 
                 "(" + self.generalize_regex_pattern(s["text"]) + ")" if s["type"]=="capture" else 
                 self.translate_to_regex(s["text"]))
                for s in item["segments"]
            )

        # 应用 segment 的 tags，显示灰色
        self.apply_segment_tags(item)

        # 更新右侧 regex 显示
        self.regex_text_input.delete("1.0", tk.END)
        self.regex_text_input.insert("1.0", item.get("regex", ""))

    def unmark_button_function(self):
        cursor = self.left_text_widget.index("insert")

        # 找到 cursor 所属的 highlight_item
        found_item = None
        for item in getattr(self, "highlight_items", []):
            h_start = item.get("start")
            h_end = item.get("end")
            if not h_start or not h_end:
                continue
            try:
                if (self.left_text_widget.compare(cursor, ">=", h_start) and
                    self.left_text_widget.compare(cursor, "<", h_end)):
                    found_item = item
                    break
            except Exception:
                continue

        if not found_item:
            return

        item = found_item

        # --- 1. 计算 cursor 在整个 item 内的 offset ---
        try:
            rel_cursor_off = self.left_text_widget.count(item["start"], cursor, "chars")[0]
        except Exception:
            return

        # --- 2. 找到 cursor 所在 segment ---
        pos = 0
        seg_index = None
        for i, seg in enumerate(item["segments"]):
            seg_len = len(seg["text"])
            if pos <= rel_cursor_off < pos + seg_len:
                seg_index = i
                break
            pos += seg_len

        if seg_index is None:
            return

        seg = item["segments"][seg_index]

        # --- 3. 根据 segment 类型进行处理 ---
        if seg["type"] in ("capture", "notcare"):
            # 这里调用你已有的正式函数
            self.unmark_segment(item, seg)

            # # 更新右侧 regex 显示
            # self.regex_text_input.delete("1.0", tk.END)
            # self.regex_text_input.insert("1.0", item.get("regex", ""))

            # # 高亮 group
            # try:
            #     self.highlight_capture_groups()
            # except Exception:
            #     pass
            return

        # ---------------------------------------------------------
        # 如果是 match segment → 删除整个 highlight（沿用你的旧逻辑）
        # ---------------------------------------------------------
        base_tag = item.get("tag")
        if base_tag:
            for t in list(self.left_text_widget.tag_names()):
                if str(t).startswith(str(base_tag)):
                    try:
                        self.left_text_widget.tag_remove(t, "1.0", "end")
                    except Exception:
                        pass

        # 删除 captures 的 tags
        for cap in item.get("captures", []):
            try:
                if cap.get("tag"):
                    self.left_text_widget.tag_remove(cap["tag"], "1.0", "end")
            except Exception:
                pass

        # 从列表删除
        try:
            self.highlight_items.remove(item)
        except Exception:
            pass

        # 清空 regex 显示
        try:
            self.regex_text_input.delete("1.0", tk.END)
        except Exception:
            pass

    def unmark_segment(self, item, seg_info):
        """安全地删除一个 segment 的 tag，并更新 highlight_item"""
        if not item or not seg_info:
            return

        base_tag = item.get("tag", "")
        # 尝试安全获取 segment tag
        seg_index = item["segments"].index(seg_info)
        c_tag = seg_info.get("tag")
        if not c_tag and base_tag:
            c_tag = f"{base_tag}_{seg_index}"

        # 计算 segment 在 Text 中的起止索引
        try:
            start_index = self.left_text_widget.index(f"{item['start']}+{sum(len(s['text']) for s in item['segments'][:seg_index])}c")
            end_index = self.left_text_widget.index(f"{start_index}+{len(seg_info['text'])}c")
        except Exception:
            start_index = None
            end_index = None

        # 移除该 segment 的 tag
        if c_tag:
            self.remove_tag_safe(c_tag, start=start_index, end=end_index)

        # 如果是 capture 或 notcare，转换为 match
        if seg_info.get("type") in ("capture", "notcare"):
            seg_info["type"] = "match"
            # 清空原 tag 字段（apply_segment_tags 会重新生成）
            seg_info.pop("tag", None)
        else:
            # 如果是 match 段，删除整个 highlight item
            # 移除所有 base_tag 开头的 tag
            if base_tag:
                for t in list(self.left_text_widget.tag_names()):
                    try:
                        if str(t).startswith(base_tag):
                            self.remove_tag_safe(str(t))
                    except Exception:
                        pass
            # 移除所有 captures tag
            for cap in list(item.get("captures", []) or []):
                try:
                    if cap.get("tag"):
                        self.remove_tag_safe(cap.get("tag"), cap.get("start"), cap.get("end"))
                except Exception:
                    pass
            # 从 highlight_items 中删除
            try:
                if item in self.highlight_items:
                    self.highlight_items.remove(item)
            except Exception:
                pass
            return

        # 删除 item 内原 captures 对应 segment 的记录
        try:
            if "captures" in item and isinstance(item["captures"], list):
                for cap in list(item["captures"]):
                    if cap.get("text") == seg_info.get("text"):
                        item["captures"].remove(cap)
        except Exception:
            pass

        # 合并相邻 match 段
        merged = []
        for s in item["segments"]:
            if merged and merged[-1].get("type") == s.get("type") == "match":
                merged[-1]["text"] += s["text"]
            else:
                merged.append({"text": s["text"], "type": s.get("type")})
        item["segments"] = merged

        # 如果 segments 为空，删除整个 highlight
        if not item["segments"]:
            if base_tag:
                for t in list(self.left_text_widget.tag_names()):
                    try:
                        if str(t).startswith(base_tag):
                            self.remove_tag_safe(str(t))
                    except Exception:
                        pass
            try:
                if item in self.highlight_items:
                    self.highlight_items.remove(item)
            except Exception:
                pass
            try:
                self.regex_text_input.delete("1.0", tk.END)
            except Exception:
                pass
            return

        # 更新 item["text"]
        try:
            item["text"] = "".join([s["text"] for s in item["segments"]])
        except Exception:
            pass

        # 更新 regex
        try:
            item["regex"] = self.build_regex_from_segments(item)
        except Exception:
            try:
                item["regex"] = "".join([
                    "(" + self.generalize_regex_pattern(s["text"]) + ")" if s["type"]=="capture" else
                    r"[\s\S]*?" if s["type"]=="notcare" else self.translate_to_regex(s["text"])
                    for s in item["segments"]
                ])
            except Exception:
                item["regex"] = item.get("regex", "")

        # 重新应用 tag
        try:
            self.apply_segment_tags(item)
        except Exception:
            pass

        # 更新右侧显示
        try:
            self.regex_text_input.delete("1.0", tk.END)
            self.regex_text_input.insert("1.0", item.get("regex", ""))
            self.highlight_capture_groups()
        except Exception:
            pass

    def remove_tag_safe(self, tag, start=None, end=None):
        """安全移除 tag 并清理样式"""
        try:
            if start and end:
                self.left_text_widget.tag_remove(tag, start, end)
            else:
                ranges = self.left_text_widget.tag_ranges(tag)
                if ranges:
                    for i in range(0, len(ranges), 2):
                        self.left_text_widget.tag_remove(tag, ranges[i], ranges[i+1])
            if not self.left_text_widget.tag_ranges(tag):
                try:
                    self.left_text_widget.tag_delete(tag)
                except Exception:
                    try:
                        self.left_text_widget.tag_config(tag, foreground="", background="")
                    except Exception:
                        pass
        except Exception:
            pass

    def merge_adjacent_match_segments(self, item):
        """
        将 target_item 的主 match tag 覆盖的多个零碎区间合并为一个连续段
        （Text widget 本身可以有多个 range，所以我们手动合并）
        """
        tag = item["tag"]
        ranges = self.left_text_widget.tag_ranges(tag)

        if not ranges:
            return

        # 将 ranges 转成 [(start, end), ...]
        segments = []
        for i in range(0, len(ranges), 2):
            segments.append((ranges[i], ranges[i+1]))

        # 根据 index 排序（避免顺序错乱）
        segments.sort(key=lambda r: float(r[0]))

        # 合并连续区间
        merged = []
        cur_start, cur_end = segments[0]

        for s, e in segments[1:]:
            if self.left_text_widget.compare(s, "<=", cur_end):
                # 有重叠或紧邻 → 合并
                cur_end = e
            else:
                merged.append((cur_start, cur_end))
                cur_start, cur_end = s, e

        merged.append((cur_start, cur_end))

        # 清空原 tag
        self.left_text_widget.tag_remove(tag, "1.0", "end")

        # 添加合并后的区间
        for s, e in merged:
            self.left_text_widget.tag_add(tag, s, e)
            # 更新 item 的 start/end（用第一个区间）
            item["start"], item["end"] = merged[0]

    def rebuild_regex_from_segments(self, item):
        """
        根据当前的匹配区间（含 capture / notcare）重新构建 regex
        """
        start = item["start"]
        end = item["end"]
        hl_text = self.left_text_widget.get(start, end)

        regex = ""
        cur_index = 0

        # 按 capture 排序
        caps = sorted(item.get("captures", []),
                      key=lambda c: float(c["start"]))

        for cap in caps:
            rel_s = self.left_text_widget.count(start, cap["start"], "chars")[0]
            rel_e = self.left_text_widget.count(start, cap["end"], "chars")[0]

            # 普通区域
            normal_text = hl_text[cur_index:rel_s]
            regex += self.translate_to_regex(normal_text)

            # capture / notcare 段
            regex += cap["capture_regex"]

            cur_index = rel_e

        # 最后尾部部分
        tail_text = hl_text[cur_index:]
        regex += self.translate_to_regex(tail_text)

        item["regex"] = regex

    def merge_regex_nodes(self,pattern):
        """
        将正则表达式解析成节点列表，并合并相同类型的连续字符
        节点类型：
            - fixed: 固定字符
            - digit: 数字
            - word: 英文字符
            - chinese: 中文字符
            - space: 空白符
            - special: 其他特殊字符
        返回：
            [{"type": 类型, "content": 内容, "quantifier": 量词}, ...]
        """
        nodes = []
        # 匹配中文、英文、数字、空白、特殊字符
        i = 0
        n = len(pattern)
    
        def get_type(c):
            if c.isdigit():
                return "digit"
            elif re.match(r"[a-zA-Z]", c):
                return "word"
            elif re.match(r"[\u4e00-\u9fff]", c):
                return "chinese"
            elif c.isspace():
                return "space"
            else:
                return "special"

        while i < n:
            c = pattern[i]
            node_type = get_type(c)
            content = c
            quantifier = ""

            # 检查是否有量词在字符后面
            if i + 1 < n and pattern[i + 1] in "*+?":
                quantifier = pattern[i + 1]
                i += 1

            # 合并连续相同类型字符
            j = i + 1
            while j < n:
                c2 = pattern[j]
                t2 = get_type(c2)
                if t2 == node_type:
                    # 检查是否有量词在后面
                    if j + 1 < n and pattern[j + 1] in "*+?":
                        content += c2
                        quantifier += pattern[j + 1]
                        j += 2
                        continue
                    content += c2
                    j += 1
                else:
                    break

            nodes.append({"type": node_type, "content": content, "quantifier": quantifier})
            i = j

        return nodes

    def run_button_function(self):
        """执行正则匹配功能"""

        mode = self.match_mode_value.get()
        input_text = self.left_text_widget.get("1.0", "end").rstrip("\n")
        regex_list = [item.get("regex") for item in self.highlight_items if "regex" in item]

        if not regex_list:
            messagebox.showerror("Error", "No regex rules found in highlight_items.")
            return

        if not input_text.strip():
            messagebox.showerror("Error", "Left text area is empty.")
            return

        if mode not in (0, 1):
            messagebox.showerror("Error", "match_mode_value is invalid.")
            return

        self.right_text_widget.delete("1.0", "end")

        # ---------------------- 模式 0：独立匹配 ----------------------
        if mode == 0:
            columns = []
            row_numbers = []

            for regex in regex_list:
                try:
                    matches = list(re.finditer(regex, input_text))
                except Exception as e:
                    messagebox.showerror("Regex Error", f"Invalid regex:\n{regex}\n\n{e}")
                    return

                col_vals = []
                col_rows = []

                for m in matches:
                    # 处理匹配值，替换换行符为4个空格
                    if m.lastindex:
                        val = " | ".join(m.group(i).replace("\n", "    ") for i in range(1, m.lastindex + 1))
                    else:
                        val = m.group(0).replace("\n", "    ")
                    col_vals.append(val)

                    if self.show_row_number_value.get() == 1:
                        line_no = input_text[:m.start()].count("\n") + 1
                        col_rows.append(str(line_no))

                columns.append(col_vals)
                row_numbers.append(col_rows)

            # ---------- 统计每列行数 ----------
            counts_line_parts = []
            for col_idx, col in enumerate(columns):
                if self.show_row_number_value.get() == 1:
                    counts_line_parts.append("line")
                counts_line_parts.append(str(len(col)))
            counts_line = "\t\t".join(counts_line_parts)

            # ---------- 组装结果行 ----------
            max_rows = max(len(col) for col in columns)
            result_lines = []

            for row in range(max_rows):
                row_parts = []
                for col_idx, col in enumerate(columns):
                    # 行号列
                    if self.show_row_number_value.get() == 1:
                        if row < len(row_numbers[col_idx]):
                            row_parts.append(row_numbers[col_idx][row])
                        else:
                            row_parts.append("")
                    # capture列
                    if row < len(col):
                        row_parts.append(col[row])
                    else:
                        row_parts.append("")
                result_lines.append("\t\t".join(row_parts))

            self.right_text_widget.insert("1.0", counts_line + "\n" + "\n".join(result_lines))
            return

        # ---------------------- 模式 1：顺序匹配 ----------------------
        elif mode == 1:
            text = input_text
            results = []

            while text.strip():
                row = []
                row_lines = []
                remaining = text

                for regex in regex_list:
                    try:
                        match = re.search(regex, remaining)
                    except Exception as e:
                        messagebox.showerror("Regex Error", f"Invalid regex:\n{regex}\n\n{e}")
                        return

                    if not match:
                        # 输出前统计行
                        counts_line_parts = []
                        for col in regex_list:
                            if self.show_row_number_value.get() == 1:
                                counts_line_parts.append("line")
                            counts_line_parts.append(str(len(results)))
                        counts_line = "\t\t".join(counts_line_parts)
                        if results:
                            self.right_text_widget.insert("1.0", counts_line + "\n" + "\n".join(results))
                        return

                    # capture 或整体，替换换行符为4个空格
                    if match.lastindex:
                        val = " | ".join(match.group(i).replace("\n", "    ") for i in range(1, match.lastindex + 1))
                    else:
                        val = match.group(0).replace("\n", "    ")
                    row.append(val)

                    # 行号
                    if self.show_row_number_value.get() == 1:
                        line_no = input_text[:text.find(match.group(0))].count("\n") + 1
                        row_lines.append(str(line_no))

                    remaining = remaining[match.end():]

                # 插入交替的行号和 capture
                if self.show_row_number_value.get() == 1:
                    interleaved_row = []
                    for ln, val in zip(row_lines, row):
                        interleaved_row.append(ln)
                        interleaved_row.append(val)
                    results.append("\t\t".join(interleaved_row))
                else:
                    results.append("\t\t".join(row))

                text = remaining

            # 输出最终结果
            counts_line_parts = []
            for col in regex_list:
                if self.show_row_number_value.get() == 1:
                    counts_line_parts.append("line")
                counts_line_parts.append(str(len(results)))
            counts_line = "\t\t".join(counts_line_parts)
            self.right_text_widget.insert("1.0", counts_line + "\n" + "\n".join(results))

    def highlight_capture_groups(self):
        text = self.regex_text_input.get("1.0", "end")

        # 清除旧的 tag
        self.regex_text_input.tag_remove("capture_group", "1.0", "end")

        stack = []
        groups = []

        i = 0
        n = len(text)

        while i < n:
            ch = text[i]

            # 计算 ch 前面连续的反斜杠数量
            bs_count = 0
            j = i - 1
            while j >= 0 and text[j] == '\\':
                bs_count += 1
                j -= 1

            is_escaped = (bs_count % 2 == 1)

            if ch == '(' and not is_escaped:
                stack.append(i)

            elif ch == ')' and not is_escaped:
                if stack:
                    start = stack.pop()
                    end = i + 1
                    groups.append((start, end))

            i += 1

        # 高亮所有捕获组
        for start, end in groups:
            start_index = f"1.0 + {start} chars"
            end_index = f"1.0 + {end} chars"
            self.regex_text_input.tag_add("capture_group", start_index, end_index)

    def update_highlight_items(self, event=None):
        """把 regex_text_input 当前行的文本，更新到对应的 highlight_item（基于 left_text_widget 的光标位置判定）"""

        # 读取右侧单行/多行编辑区当前行文本（如果你右侧是单行可直接取全部）
        # 这里取当前光标所在的整行内容
        try:
            # 如果 regex_text_input 是单行输入，也可以直接用 get("1.0", "end").strip()
            r_index = self.regex_text_input.index("insert")
            r_line_no = int(r_index.split('.')[0])
            text = self.regex_text_input.get(f"{r_line_no}.0", f"{r_line_no}.end").strip()
        except Exception:
            # 回退：读取全部
            text = self.regex_text_input.get("1.0", "end").strip()

        # 取左侧光标位置，用于判断属于哪个 highlight_item
        try:
            cursor = self.left_text_widget.index("insert")
        except Exception:
            cursor = None

        # 确保 highlight_items 存在
        if not hasattr(self, "highlight_items") or self.highlight_items is None:
            self.highlight_items = []

        # 若有有效左侧光标，则找到包含该光标的 item 并更新其 regex
        if cursor:
            for item in self.highlight_items:
                s = item.get("start")
                e = item.get("end")
                if not s or not e:
                    continue
                try:
                    if (self.left_text_widget.compare(cursor, ">=", s) and
                        self.left_text_widget.compare(cursor, "<=", e)):
                        # 找到对应 item，更新其 regex 字段
                        item["regex"] = text
                        return
                except Exception:
                    # compare 可能因索引格式问题失败，跳过该 item
                    continue

        # 如果没找到对应项（可能是新建），则追加一个新 item（保留 start/end 为 None）
        new_item = {
            "regex": text,
            "start": None,
            "end": None,
            "tag": None,
            "captures": [],
        }
        self.highlight_items.append(new_item)

    def generalize_regex_pattern(self, text):
        t = text.strip()

        # --- 1. 0x 开头的 hex ---
        if re.fullmatch(r"0[xX][A-Fa-f0-9]+", t):
            return r"0x[A-Fa-f0-9]+"

        # --- 2. Hex 字符串 ---
        if re.fullmatch(r"[A-Fa-f0-9]{2,}", t):
            return r"[A-Fa-f0-9]+"

        # --- 3. 数值 (整数、小数、负数) ---
        if re.fullmatch(r"-?\d+(?:\.\d+)?", t):
            return r"-?\d+(?:\.\d+)?"

        # --- 4. IPv4 ---
        if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", t):
            return r"(?:\d{1,3}\.){3}\d{1,3}"

        # --- 5. MAC 地址 ---
        if re.fullmatch(r"[A-Fa-f0-9]{2}(?:[:-][A-Fa-f0-9]{2}){5}", t):
            return r"[A-Fa-f0-9]{2}(?:[:-][A-Fa-f0-9]{2}){5}"

        # --- 6. 日期 YYYY-MM-DD / YYYY/MM/DD ---
        if re.fullmatch(r"\d{4}[-/]\d{1,2}[-/]\d{1,2}", t):
            return r"\d{4}[-/]\d{1,2}[-/]\d{1,2}"

        # --- 7. 时间 HH:MM[:SS] ---
        if re.fullmatch(r"\d{1,2}:\d{2}(?::\d{2})?", t):
            return r"\d{1,2}:\d{2}(?::\d{2})?"

        # --- 8. 字母数字混合 ---
        if re.fullmatch(r"[A-Za-z0-9]+", t):
            return r"[A-Za-z0-9]+"

        # --- 9. 字母数字空格混合 ---
        if re.fullmatch(r"[A-Za-z0-9\s]+", t):
            return r"[A-Za-z0-9\s\n]*?"

        # --- 9.1 英文数字空格及常用符号 ---
        if re.fullmatch(r"[A-Za-z0-9\s!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:'\",.<>/?\\|`~]+", t):
            return r"[A-Za-z0-9\s!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:'\",.<>/?\\|`~\n]*?"

        # --- 10. 中文 ---
        if re.fullmatch(r"[\u4e00-\u9fa5]+", t):
            return r"[\u4e00-\u9fa5]+"

        # --- 11. 中文 + 英文 ---
        if re.fullmatch(r"[\u4e00-\u9fa5A-Za-z]+", t):
            return r"[\u4e00-\u9fa5A-Za-z]+"

        # --- 12. 中文 + 英文 + 数字 ---
        if re.fullmatch(r"[\u4e00-\u9fa5A-Za-z0-9]+", t):
            return r"[\u4e00-\u9fa5A-Za-z0-9]+"

        # --- 13. 中文 + 英文 + 数字 + 空格 + 中文符号 + 换行 ---
        if re.fullmatch(r"[\u4e00-\u9fa5A-Za-z0-9\s，。！？；：”“‘’（）《》\n]+", t):
            return r"[\u4e00-\u9fa5A-Za-z0-9\s，。！？；：”“‘’（）《》\n]+"

        return self.translate_to_regex(text)

    def split_segments(self, item, abs_sel_start, abs_sel_end):
        """
        将 highlight_item 的 segments 根据选中区间切分成更细的段。
        abs_sel_start / abs_sel_end 是绝对文本坐标（Text widget index）
        """

        hl_start = item["start"]

        # 转换为相对 offset
        rel_start = self.left_text_widget.count(hl_start, abs_sel_start, "chars")[0]
        rel_end   = self.left_text_widget.count(hl_start, abs_sel_end, "chars")[0]

        new_segments = []
        pos = 0

        for seg in item["segments"]:
            t = seg["text"]
            seg_len = len(t)

            if pos + seg_len <= rel_start or pos >= rel_end:
                # 与选区无交集 → 保持原样
                new_segments.append(seg)
            else:
                # 有交集 → 分三段

                # 1) 左边残留
                left_len = max(0, rel_start - pos)
                if left_len > 0:
                    new_segments.append({
                        "text": t[:left_len],
                        "type": seg["type"]
                    })

                # 2) 中间选中部分
                mid_start = max(0, rel_start - pos)
                mid_end   = min(seg_len, rel_end - pos)
                if mid_start < mid_end:
                    new_segments.append({
                        "text": t[mid_start:mid_end],
                        "type": None    # 稍后赋值（capture / notcare）
                    })

                # 3) 右边残留
                right_len = seg_len - mid_end
                if right_len > 0:
                    new_segments.append({
                        "text": t[mid_end:],
                        "type": seg["type"]
                    })

            pos += seg_len

        item["segments"] = new_segments
        return new_segments

    def load_regex_button_function(self):
        # -------------------------------------------------------------
        # 1. 选择文件
        # -------------------------------------------------------------
        file_path = fd.askopenfilename(
            title="选择 Regex TXT 文件",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not file_path:  # 用户取消
            return

        # -------------------------------------------------------------
        # 2. 读取文件
        # -------------------------------------------------------------
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = [line.strip() for line in f.readlines()]
        except Exception as e:
            messagebox.showerror("Error", f"Coulnd not read file：\n{e}")
            return

        # 去掉空行
        regex_list = [ln for ln in lines if ln]

        if not regex_list:
            messagebox.showwarning("Warning", "File empty, no regex found！")
            return

        # -------------------------------------------------------------
        # 3. 清除当前 highlight_items
        # -------------------------------------------------------------
        self.highlight_items.clear()

        # 记录过程中所有的错误
        error_messages = []

        # 输入文本
        full_text = self.left_text_widget.get("1.0", "end")

        # -------------------------------------------------------------
        # 4. 对每一行 regex 执行同样的逻辑
        # -------------------------------------------------------------
        for regex in regex_list:
            try:
                pattern = re.compile(regex)
            except Exception as e:
                error_messages.append(f"Regex 编译失败: {regex}\n{e}")
                continue

            match = pattern.search(full_text)
            if not match:
                error_messages.append(f"未匹配到内容: {regex}")
                continue

            # ---------------------------------------------------------
            # 4.1 选中第一个匹配内容 → run mark_as_mark_button_function
            # ---------------------------------------------------------
            start_idx = f"1.0+{match.start()}c"
            end_idx   = f"1.0+{match.end()}c"

            try:
                self.left_text_widget.tag_remove("sel", "1.0", "end")
                self.left_text_widget.tag_add("sel", start_idx, end_idx)
                self.mark_as_mark_button_function()
            except Exception as e:
                error_messages.append(f"mark_as_mark_button_function 失败: {regex}\n{e}")
                continue

            # ---------------------------------------------------------
            # 4.2 对其所有 capture group 执行 mark_as_target_button_function
            # ---------------------------------------------------------
            if match.lastindex:  # 有捕获组
                for i in range(1, match.lastindex + 1):
                    try:
                        g_start = match.start(i)
                        g_end   = match.end(i)

                        if g_start == -1 or g_end == -1:
                            continue

                        g_start_idx = f"1.0+{g_start}c"
                        g_end_idx   = f"1.0+{g_end}c"

                        self.left_text_widget.tag_remove("sel", "1.0", "end")
                        self.left_text_widget.tag_add("sel", g_start_idx, g_end_idx)
                        self.mark_as_target_button_function()
                    except Exception as e:
                        error_messages.append(
                            f"mark_as_target_button_function 失败: {regex}\n捕获组 {i}\n{e}"
                        )
                        continue



        # -------------------------------------------------------------
        # 5. 更新 highlight_items 中所有 regex 为 TXT 文件中的内容（带异常处理）
        # -------------------------------------------------------------
        for idx, regex in enumerate(regex_list):
            try:
                if idx < len(self.highlight_items):
                    self.highlight_items[idx]["regex"] = regex
            except Exception as e:
                error_messages.append(f"更新 highlight_item regex 失败，索引 {idx}：{e}")

        # -------------------------------------------------------------
        # 6. 若有错误 → 展示所有错误
        # -------------------------------------------------------------
        if error_messages:
            messagebox.showwarning("Regex Load Finished With Errors", "\n\n".join(error_messages))
        else:
            messagebox.showinfo("Success", "All Regex loaded and applied.")

    def save_regex_button_function(self):
        # -------------------------
        # 1. 检查是否有 regex 可保存
        # -------------------------
        if not hasattr(self, "highlight_items") or len(self.highlight_items) == 0:
            messagebox.showwarning("Warning", "No Regex found！")
            return

        # 收集 regex
        regex_list = []
        for item in self.highlight_items:
            if "regex" in item and item["regex"]:
                regex_list.append(item["regex"])

        if len(regex_list) == 0:
            messagebox.showwarning("Warning", "No Regex found！")
            return

        # -------------------------
        # 2. 弹出保存文件窗口
        # -------------------------
        file_path = fd.asksaveasfilename(
            title="保存 Regex 文件",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not file_path:  # 用户取消
            return

        # -------------------------
        # 3. 保存到文件
        # -------------------------
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                for regex in regex_list:
                    f.write(regex + "\n")

            messagebox.showinfo("Success", f"Regex successfully save to：\n{file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"File save fail：\n{e}")

    def focus_to_last_regex_button_function(self):
        """跳到上一个 highlight item 的行首（基于 highlight_items 的 start/end）"""
        # 必要性检查
        if not hasattr(self, "highlight_items") or not self.highlight_items:
            messagebox.showinfo("Info", "No highlight items.")
            return

        # 将 start 转为可排序的 tuple (line, col)
        def index_to_tuple(index):
            try:
                s = str(index)
                line, col = s.split(".")
                return int(line), int(col)
            except Exception:
                return (10**9, 10**9)  # 放到最后

        # 收集所有有效 item 的 start/end（跳过没有 start 的）
        items = []
        for it in self.highlight_items:
            s = it.get("start")
            e = it.get("end")
            if not s or not e:
                continue
            items.append((s, e, it))

        if not items:
            messagebox.showinfo("Info", "No valid highlight items with start/end.")
            return

        # 按 start 排序
        items.sort(key=lambda x: index_to_tuple(x[0]))

        # 当前光标位置
        try:
            cur = self.left_text_widget.index("insert")
        except Exception:
            cur = None

        # 如果光标在某个 item 内，则找到该 item 的索引
        cur_idx = None
        if cur:
            for i, (s, e, it) in enumerate(items):
                try:
                    if (self.left_text_widget.compare(cur, ">=", s) and
                        self.left_text_widget.compare(cur, "<=", e)):
                        cur_idx = i
                        break
                except Exception:
                    continue

        # 如果没有在任一 item 内，用 start 与 cur 比较找到前一个 item（start < cur）
        if cur_idx is None and cur:
            prev_i = None
            for i, (s, e, it) in enumerate(items):
                try:
                    if self.left_text_widget.compare(s, "<", cur):
                        prev_i = i
                    else:
                        break
                except Exception:
                    continue
            if prev_i is None:
                messagebox.showinfo("Info", "Already before the first match (no previous match).")
                return
            target_item = items[prev_i]
        else:
            # cur_idx is index of current item; we want previous item
            if cur_idx is None:
                # 没有光标信息，直接取最后一个可用项作为目标
                target_item = items[-1]
            else:
                prev_index = cur_idx - 1
                if prev_index < 0:
                    messagebox.showinfo("Info", "Already at the first match.")
                    return
                target_item = items[prev_index]

        # target_item 是 (start, end, it)
        tgt_start = target_item[0]
        # 计算行首位置
        try:
            line_no = int(str(tgt_start).split(".")[0])
            line_start = f"{line_no}.0"
        except Exception:
            line_start = tgt_start  # fallback

        # 移动光标并滚动视图
        try:
            self.left_text_widget.mark_set("insert", line_start)
            self.left_text_widget.see(line_start)
            # 取消选区，确保视觉正常
            try:
                self.left_text_widget.tag_remove("sel", "1.0", "end")
            except Exception:
                pass
        except Exception:
            messagebox.showerror("Error", "Failed to move cursor to previous match.")

        self.on_cursor_move_highlight()     # 让regex同步显示
        self.left_text_widget.focus_set()   # 关键步骤，光标恢复闪烁


    def focus_to_next_regex_button_function(self):
        """跳到下一个 highlight item 的行首（基于 highlight_items 的 start/end）"""
        if not hasattr(self, "highlight_items") or not self.highlight_items:
            messagebox.showinfo("Info", "No highlight items.")
            return

        def index_to_tuple(index):
            try:
                s = str(index)
                line, col = s.split(".")
                return int(line), int(col)
            except Exception:
                return (10**9, 10**9)

        items = []
        for it in self.highlight_items:
            s = it.get("start")
            e = it.get("end")
            if not s or not e:
                continue
            items.append((s, e, it))

        if not items:
            messagebox.showinfo("Info", "No valid highlight items with start/end.")
            return

        items.sort(key=lambda x: index_to_tuple(x[0]))

        try:
            cur = self.left_text_widget.index("insert")
        except Exception:
            cur = None

        cur_idx = None
        if cur:
            for i, (s, e, it) in enumerate(items):
                try:
                    if (self.left_text_widget.compare(cur, ">=", s) and
                        self.left_text_widget.compare(cur, "<=", e)):
                        cur_idx = i
                        break
                except Exception:
                    continue

        # 如果不在任何 item 内，则找到第一个 start > cur 的 item
        if cur_idx is None and cur:
            next_i = None
            for i, (s, e, it) in enumerate(items):
                try:
                    if self.left_text_widget.compare(s, ">", cur):
                        next_i = i
                        break
                except Exception:
                    continue
            if next_i is None:
                messagebox.showinfo("Info", "Already after the last match (no next match).")
                return
            target_item = items[next_i]
        else:
            # 在某个 item 内，跳到下一个
            if cur_idx is None:
                # 没有光标信息，取第一个
                target_item = items[0]
            else:
                next_index = cur_idx + 1
                if next_index >= len(items):
                    messagebox.showinfo("Info", "Already at the last match.")
                    return
                target_item = items[next_index]

        tgt_start = target_item[0]
        try:
            line_no = int(str(tgt_start).split(".")[0])
            line_start = f"{line_no}.0"
        except Exception:
            line_start = tgt_start

        try:
            self.left_text_widget.mark_set("insert", line_start)
            self.left_text_widget.see(line_start)
            try:
                self.left_text_widget.tag_remove("sel", "1.0", "end")
            except Exception:
                pass
        except Exception:
            messagebox.showerror("Error", "Failed to move cursor to next match.")

        self.on_cursor_move_highlight()     # 让regex同步显示
        self.left_text_widget.focus_set()   # 关键步骤，光标恢复闪烁

    def show_regex_table_function(self):
        """弹出一个窗口，展示常用泛化正则表达式表"""
        # 新建窗口
        win = tk.Toplevel(self)
        win.title("常用泛化正则表达式表")
        win.geometry("1200x270")

        # 文本区域
        text_area = tk.Text(win, wrap="none", font=("Sarasa Mono SC", 12))
        text_area.pack(fill="both", expand=True, padx=10, pady=5)

        # 表格内容
        table_content = r"""NO.     匹配类型                  示例                    泛化正则表达式                                   说明
 1  0x十六进制数              0x1A3F                 0x[A-Fa-f0-9]+                                   匹配 0x 或 0X 开头的任意长度 hex
 2  十六进制数                1A3F                   [A-Fa-f0-9]+                                     任意长度十六进制字符串
 3  数值                      123, -45.6             -?\d+(?:\.\d+)?                                  整数、浮点数、负数
 4  IPv4地址                  192.168.0.1            (?:\d{1,3}\.){3}\d{1,3}                          典型 IPv4 地址
 5  MAC地址                   01:23:45:67:89:AB      [A-Fa-f0-9]{2}(?:[:-][A-Fa-f0-9]{2}){5}          MAC 地址，可用冒号或短横分隔
 6  日期                      2025-12-09             \d{4}[-/]\d{1,2}[-/]\d{1,2}                      YYYY-MM-DD 或 YYYY/MM/DD
 7  时间                      14:30 或 14:30:59      \d{1,2}:\d{2}(?::\d{2})?                         HH:MM 或 HH:MM:SS
 8  字母数字                  abc123                 [A-Za-z0-9]+                                     仅字母和数字
 9  字母数字空格              abc 123                [A-Za-z0-9\s]+                                   允许字母、数字及空格
10  中文                      中文                   [\u4e00-\u9fff]+                                 匹配中文字符
11  中文+英文                 中文abc                [\u4e00-\u9fffA-Za-z]+                           中文和英文混合
12  中文+英文+数字            中文abc123             [\u4e00-\u9fffA-Za-z0-9]+                        中文、英文、数字混合
13  中文+英文+数字+空格符号   中文 abc123,。         [\u4e00-\u9fffA-Za-z0-9\s\p{P}]+                 中文、英文、数字、空格、标点符号混合
"""

        text_area.insert("1.0", table_content)
        #text_area.config(state="disabled")  # 设置只读

    def open_regex_tutorial_function(self):
        """直接打开默认浏览器，跳转到 Python 正则表达式教程"""
        try:
            webbrowser.open("https://deerchao.cn/tutorials/regex/regex.htm?utm_source=chatgpt.com")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not open browser:\n{e}")

    def save_as_button_function(self):
        try:
            # 1. 获取文本内容
            content = self.right_text_widget.get("1.0", "end-1c")

            # 2. 选择保存位置
            file_path = fd.asksaveasfilename(
                title="Save As",
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )

            # 用户取消
            if not file_path:
                return  

            # 3. 写文件
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            # 4. 成功提示
            mb.showinfo("Saved", f"File saved to:\n{file_path}")

        except Exception as e:
            mb.showerror("Error", f"Failed to save file:\n{e}")

    def show_about_window(self):
        top = tk.Toplevel(self)
        top.title("Donation")
        # 设置固定窗口大小
        win_width = 300
        win_height = 300

        # 获取主窗口的位置和尺寸
        self.update_idletasks()
        root_x = self.winfo_x()
        root_y = self.winfo_y()
        root_width = self.winfo_width()
        root_height = self.winfo_height()

        # 计算居中位置
        pos_x = root_x + (root_width - win_width) // 2
        pos_y = root_y + (root_height - win_height) // 2

        # 设置 Toplevel 窗口的大小和位置
        top.geometry(f"{win_width}x{win_height}+{pos_x}+{pos_y}")
    
        # 加载大图
        try:
            # 解码 base64 数据
            img_data = base64.b64decode(img_base64)
            img_pil = Image.open(BytesIO(img_data))
            img_resized = img_pil.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img_resized)

            # 显示图片
            label = tk.Label(top, image=photo)
            label.image = photo  # 防止被垃圾回收
            label.pack(pady=10)
        except Exception as e:
            tk.Label(top, text=f"图片显示失败: {e}").pack()

        tk.Label(top, text="Open source is not easy.").pack()
        tk.Label(top, text="Donations are welcome via Alipay.").pack()

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()

