# BitSoc

# Description About Files:

The main_blockchain.py file is the main code file for the P.S. 

Blockchain.ipynb is the jupyter version of main_blockchain.py file.

# Input

mempool.csv is the input csv file which contains,  
<txid>,<fee>,<weight>,<parent_txids>
txid is the transaction identifier
fee is the transaction fee
weight is the transaction weight
parent_txids is a list of the txids of the transaction’s unconfirmed parent transactions 
(confirmed parent transactions are not included in this list). It is of
the form: <txid1>;<txid2>;...
  
  

  
# Output
  
block.txt is our output text file containing the txids based on the P.S.
  
response.json is visualisation of our blockchain by using flask by running on HTTP Client, like Postman or cURL.
  


  




