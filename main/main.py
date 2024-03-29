# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import blockchain.chain
import blockchain.wallet
import encrypt


def part_one():
    block = blockchain.chain.ChainManager().main_chain.blocks[0]
    header = {'version': block.version, 'prev_hash': block.prev_hash, 'merkle_hash': block.merkle_hash, 'bits': block.bits, 'nonce': block.nonce, 'stamp': block.stamp}
    print('欢迎来到NaiveBitCoin第1章：区块链。\n\n首先，我们了解一下什么是区块链。\n一句话概括，区块链是一种特殊的分布式数据库。\n\n首先，它主要作用是储存信息，任何需要储存的信息，都可以写入区块链。'
          '\n其次，任何人都可以架设服务器，加入区块链网络，成为一个节点，每一个节点都是平等的，你可以向任何一个节点写入/读取数据，最后所有的节点都会同步，保证区块链一致。\n\n实际上，分布式数据库并非新发明。'
          '区块链有什么特点呢？\n区块链区别于其他分布式数据库的革命性特征在于，其他的数据库都是有管理员的，但是区块链没有。\n\n没有管理员，每个人都可以往节点中写入数据，那么如何保证数据是可信的、一致的呢？'
          '\n\n让我们来了解一下区块链的基本组成：区块（Block）。\n区块包含区块头和区块体。区块体记录当前区块的元信息，区块体记录的是实际数据。\n\n以下是一个区块头的基本构成：\n\n%s\n\n区块头'
          '包含了version、prev_hash、merkle_hash、bits、nonce和stamp等信息。\n\nversion是，\n\nprev_hash是前一个区块的哈希值（Hash），\n\nmerkle_hash是当前区块存储的内容（一般而言，是交易内容）'
          '的哈希值，\n\nbits和区块形成的速度有关，\n\nnonce是随机数，和我们常说的“挖矿”息息相关，\n\nstamp是时间戳，下面我们会对这些内容进行进一步的讲解。\n\n整个区块头的哈希值就是区块的ID，和区块是一'
          '一对应的。\n上面我们看到的区块头，它的哈希值如下：\n%s\n这里我们要说明一下哈希的概念。哈希，实际上是一种函数，它接受一段数据作为输入，然后生成一段固定长度的数据作为输出，作为输入数据的'
          '签名。从理论上来说，设计良好的哈希函数，对于任何不同的输入数据，都应该以极高的概率生成不同的输出数据，也就是哈希函数具有“抗碰撞能力”；\n\n同时，即使只改变了原始数据的一个字节，所获得的哈希值都会完'
          '全不同，即哈希函数具有“抗篡改能力”。\n\n接下来你可以尝试一下，输入一串字符串，我们会使用SHA256算法对它进行HASH。\n\n' % (header, block.id))
    try_str = input()
    print('\n\n这就是哈希之后得到的结果。\n%s\n\n需要说明的'
          '是，SHA256只是一种哈希算法，NaiveBitCoin使用的就是SHA256，除此以外，哈希算法还有MD5，SHA-1，SHA-2等等。\n\n每一个区块的区块头都包含着前一个区块的HASH，就像每一个区块都指向前一个区块，就像链条'
          '一般。这就是“区块链”的由来。\n\n正是因为哈希的抗碰撞能力和抗篡改能力，我们能够用区块头的HASH值来一一对应区块。\n\n之前我们讲过，区块链本质上是一个分布式的数据库，而区块是区块链的组成部分。任何人都'
          '可以架设服务器加入区块链，成为其中一个节点，每一个节点都存储着完整的区块链，每一个区块之中存储着从上一个区块生成到本区块生成时所产生的所有数据。以比特币为例，就是存储着上一个区块生成到本区块生成时的'
          '所有交易数据。\n\n怎样才算生成一个新的区块呢？从上一个区块生成以来发生的所有交易的信息都会被存储在一个临时的未经验证的交易池之中，平均每1分钟，矿工们都会从交易池中导出交易，放到区块之中，然后通过调'
          '整上述我们提到过的，区块头中的Nonce值，使得整个区块头的哈希值满足某些设定的条件，等到Nonce值计算成功的时候，就算生成一个新的区块了。\n\n由于必须保证每个节点之间的同步，新区块的添加速度不能太快。'
          'NaiveBitCoin的设定是每过1分钟，才能产生一个新的区块，这种速率的控制不是通过命令达成的，而是通过增大计算量达成的，也就是将整个区块头的哈希值要满足的条件设置得更为苛刻一些。\n\n考虑到所有节点的算力'
          '是在动态变化的，每生成600个区块都会调整一次计算难度，如果生成这600个区块的时间超过60*60*10=36000s即10小时，就会下调难度，反之，则会上调难度，以保证每个区块平均生成的时间都是1分钟。\n\n当矿工计算'
          '出相符的Nonce值，也就是挖矿成功之后，矿工会获得相应的奖励，包括挖矿的奖励（一定量的NaiveBitCoin）和区块所记录的所有交易产生的手续费。矿工所获得的挖矿奖励随着区块的数量上涨是在下降的，直到最后区块'
          '的产生已经不再为矿工带来奖励，只给矿工带来手续费的收益，这时候NaiveBitCoin的总量就已经确定了。\n\n由于不同的节点同时挖矿，可能记录的交易会有不同，这就导致了不同的节点所记录的区块在某个时间节点上会'
          '出现分叉。那么我们怎么确定哪一个才是真正的数据？这里，我们采用了一种叫做“工作量证明”的方法，也就是说，当两个链条出现了分叉的时候，我们以长度更长的链条作为“主链”，另一条作为“次链”，次链最终都会消亡，'
          '被主链所替代。\n\n接下来，你可以自由探索，体验一下挖矿和区块链形成的过程。\n' % encrypt.sha(try_str))


def part_two():
    signing_key, verifying_key, my_address = blockchain.wallet.init_wallet()
    print('欢迎来到NaiveBitCoin第2章：电子货币与交易。\n\n电子货币可以做传统货币能做的所有事情，比如买卖商品，给个人或者组织汇款、贷款等。但，不同于传统货币，电子货币不但没有实体，而且本质上也没有一种虚拟的物品代表它。用户只要拥有证明其控制权的密钥，用密钥解锁，就可以进行交易。拥有密钥是使用电子货币的唯一条件。\n\n接下来，你会使用我们虚构的电子货币NaiveBitCoin来体验电子货币的交易过程。\n\n你首先需要获得一个钱包，这个钱包相当于你的银行账户，它对应你所拥有的货币。\n\n这个钱包包含签名密钥、验证密钥和地址等信息。\n\n%s\n每一次进行交易的时候，你要使用签名密钥来进行签名，相当于在账单上签署你的名字。\n\n%s\n这是公开的，其他人可以使用验证密钥，验证账单上你的签名是否确实是你的签名。\n\n%s\n这是你的钱包地址，别人可以向这个地址转账，相当于你的银行卡号。\n你也需要了解别人的钱包地址，才能给别人转账。\n\n当你创建了一个交易，从你自己的钱包向别的钱包转账时，你会使用签名密钥进行签名，代表你许可这笔交易对应的资金转移使用权。接下来，这笔交易会被广播到网络中，每一个节点都会进行验证、并进行广播，直到这笔交易被大多数的节点所接收。此时，这笔交易会记录在交易池中。最终，这笔交易被一个挖矿节点验证，添加到一个区块之中，并被足够多的后续区块确认，就会成为总账簿的一部分，被所有的参与者认可为有效交易，这时这笔资金的使用权才真正转移到新的参与者手上。\n\n相信现在你已经对电子货币和交易过程有了一定的了解，接下来，不要大意地尝试一下使用NaiveBitCoin来进行一次交易吧！\n' % (signing_key.to_string(), verifying_key.to_string(), my_address.decode('utf-8')))


def main():
    print(
        '欢迎来到NaiveBitCoin。接下来，我们将共同学习什么是区块链。\n\n我们的课程包括两个章节：第一章是区块链，讲述区块链的本质、区块的结构、区块的产生、区块链的构成、主链和次链等概念。\n\n第二章是电子货币与交易，这里我们使用一个虚构的电子货币NaiveBitCoin作为例子来辅助理解，你会逐步了解到什么是钱包、签名密钥、验证密钥、钱包地址，电子货币是如何进行交易的，又是如何被记录的，最终又是如何被确认的。')
    while True:
        chooser = input('请选择章节:\n1. 区块链\n2. 电子货币交易\nq. 退出\n')
        if chooser == '1':
            part_one()
        elif chooser == '2':
            part_two()
        elif chooser == 'q':
            break
        else:
            continue
