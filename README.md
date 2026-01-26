
<img width="1208" height="858" alt="image" src="https://github.com/user-attachments/assets/57a20d1f-de2c-40c6-9d31-3526a8b4061d" />


TextCatcher read me document - 最后由 吴宪 编辑于 2025.12.09

TextCatcher-RegexTester 是一个基于Python的正则表达式文本提取工具，可帮助用户从冗长的文本中提取出想要的文本，匹配的模式可以通过选择文本和点击按键的方式自动创建，正则表达式可以简洁的生成。如果需要匹配的内容较为复杂，也可以手动修改正则表达式。

本软件由Xian Wu个人开发，为单一exe文件的GUI程序，可在windows系统上运行（如果要在其他操作系统上运行需要使用原代码重新打包），使用python 3.10和VS2022的环境，借助了ChatGPT和Gemini的帮助。

如果有任何问题和建议，可以联系 xian.wu@ericsson.com 或 dakongwuxian@gmail.com 。

exe文件的下载链接如下：

https://github.com/dakongwuxian/TextCatcher/releases


如何使用：
1、通过open file或拖动文件的方式加载需要提取的txt文件；
2、选中需要匹配的文字，点击set as match按钮；
3、选中已经设置为match的文字中需要提取的文字，点击set as capture；
4、选中已经设置为match的文字中不需要匹配的可能会变化的字符，点击set as not care；
5、通过上方的文字窗口观察和修改每段match字符对应的自动生成的regex，可以通过点击文字位置自动切换regex，也可以通过点击上下按键切换字符位置和对应的regex；
6、点击run按键，会根据已经设置好的regex自动搜索并匹配，最后结果会出现在右侧的文本框中。第一行默认是所有regex匹配的次数；
7、如果勾选了match in sequence，不会每个regex单独匹配整个文本，而是会每个regex逐一匹配一次，然后继续匹配后方的文本；
8、如果勾选了row number，会将每个匹配的结果的行号也显示在单独的一列中。
9、通过set as match、set as capture、set as not care按钮编辑好的regex，可以通过save regex按键保存；
10、通过save regex按键保存好的文件，也可以通脱load regex按键加载并匹配其他的文件。需要注意，要先打开文件，再加载regex；
11、在input中可以使用ctrl+F搜索内容和记数；
12、双击output中的内容可以让input跳转到对应的内容。

注意：
1、set as match、set as capture、set as not care按钮会按照一定的规则转化文本，并不一定能完美的匹配用户的想法，可以转化后测试观察是否满足需求，如果不满足需要手动修改regex。
2、右上方有2个按钮，可以看到常用的regex和regex教程。


TextCatcher README – Last Edit: 2025.12.09 by Xian Wu

TextCatcher-RegexTester is a Python-based text extraction tool for regular expressions. It helps users extract desired content from large amounts of text. Matching patterns can be automatically created through selection and setting, allowing regular expressions to be generated easily. For more complex matching requirements, the regular expressions can also be edited manually.

This software is developed personally by Xian Wu as a standalone GUI executable. It runs on Windows (to run on other operating systems, the original code needs to be repackaged). It uses Python 3.10 and VS2022, with assistance from ChatGPT and Gemini.

For any issue or advice, please contact xian.wu@ericsson.com or dakongwuxian@gmail.com.

exe file download link is:

https://github.com/dakongwuxian/TextCatcher/releases

How to use:

1. Load the text file to be processed using the Open File button.

2. Select the text you want to match and click the Set as Match button.

3. Within a text already set as match, select the portion you want to extract and click Set as Capture.

4. Within a text already set as match, select characters that may vary and should be ignored, then click Set as Not Care.

5. Observe and edit the automatically generated regex for each match segment in the text window above. You can switch between regex by clicking on text positions or by using the up/down buttons to navigate characters and their corresponding regex.

6. Click the Run button to automatically search and match based on the configured regex. The results will appear in the text box on the right. The first line shows the total number of matches by default.

7. If Match in Sequence is checked, each regex will match sequentially rather than matching the entire text individually, continuing from the end of the previous match.

8. If Row Number is checked, the line number of each match will be displayed in a separate column.

9. Regex configured via Set as Match, Set as Capture, and Set as Not Care can be saved using the Save Regex button.

10. Regex files saved through Save Regex can also be loaded with the Load Regex button to match other files. Note: open a file before loading regex.

Notes:

1. The Set as Match, Set as Capture, and Set as Not Care buttons follow certain rules to convert text. They may not perfectly match the user’s intent. After conversion, test the results to see if they meet your needs. Manual regex edits may be required.

2. The top-right corner has two buttons to access common regex examples and regex tutorials.

![GUI screen shot](https://github.com/user-attachments/assets/38572eea-b8fd-4f25-9dc2-e4fa127f4d6f)


