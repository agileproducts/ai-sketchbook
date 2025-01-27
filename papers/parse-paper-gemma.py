import argparse
from mlx_lm import load, generate
from pathlib import Path

def typeset(text: str):
  model, tokenizer = load("../models/mlx-gemma-2b-it")
  prompt = f"""
  Take the tuples representing the authors and their corresponding affiliation from the following text and convert them into an xml format. 
  
  {text}
  
  Separate names into first name and last name.
  Separate affiliations into deparment (where given), institution, city and country.

  """

  messages = [{"role": "user", "content": prompt}]
  prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
  text = generate(model, tokenizer, prompt=prompt, verbose=True, max_tokens=5000)

def gemma_magick(text: str):

  model, tokenizer = load("../models/mlx-gemma-2b-it")

  prompt = f"""
  Extract the list of authors and their corresponding affiliation from the following text. Return the result as a python list of tuples: 
  
  {text}
  """

  messages = [{"role": "user", "content": prompt}]
  prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
  text = generate(model, tokenizer, prompt=prompt, verbose=True,  max_tokens=5000)

  typeset(text)


def parse_paper(arxiv_id: str) -> None:
  papers_dir = Path('papers')
  paper = papers_dir / f'arxiv_{arxiv_id}.md'
  with open(paper, 'r') as file:
    content = file.read(3000) #limit to so many characters

    #temporary understanding what is going on here
    mytext = """
    Authors: DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z.F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J.L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R.J. Chen, R.L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S.S. Li , Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W.L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X.Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y.K. Li, Y.Q. Wang, Y.X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y.X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z.Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Zhen Zhang 
    
    Title: A Comprehensive Study of Machine Learning Techniques for Predicting Stock Prices. 
    
    Abstract: This paper presents a comprehensive study of various machine learning techniques for predicting stock prices. The study includes a detailed analysis of different algorithms and their performance in predicting stock prices. The results show that certain algorithms, such as Support Vector Machines (SVMs) and Random Forests, perform better than others in predicting stock prices. The study also highlights the importance of data preprocessing and feature engineering in improving the performance of machine learning models for stock price prediction.

    """

    bigtext = """

  """
    gemma_magick(content)

def main():
  parser = argparse.ArgumentParser(description='Convert a paper from arXiv given its ID')
  parser.add_argument('arxiv_id', help='The arXiv ID of the paper (e.g., 2101.12345)')
  args = parser.parse_args()

  parse_paper(args.arxiv_id)

if __name__ == '__main__':
    main()