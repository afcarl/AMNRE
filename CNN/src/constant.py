dataPath="../Data/" #The relative path of data(preprocessed as .npy format)
dataName="SML" #Tag of data
batch_size=160 #Batch size
epoch=60 #Number of training epoches
dimC=230 #dimension of CNN
dimWPE=5 #dimension of word position embedding
dimWE=50 #dimension of word embedding, same as pre-trained embeddings
filter_size=3 #size of CNN's filter
Lim=30 #Half length of position embedding
SenLen=[70,85] #Max Sentence Length for Position Embedding
MaxPos=2*Lim+1 #Length of position embedding
LangNum=2 #Number of languages
Att_dropout=0.0 #Attention's dropout probability
CNNDropout=0.5 #CNN's dropout probabilty
dimR=176 #Number of relations, determined by the dataset
learning_rate=0.001 #Learning rate
Encodered_dim=dimC #Dimension of encoder's output
dis_layers=2 #Number of discriminator's layers 
dis_hidden_dim=2048 #Discriminator's hidden size
dis_input_dropout=0.1 #Discriminator's input dropout probability
dis_dropout=0.0 #Discriminator's dropout probability between layers 
dis_smooth=0.1 #Discriminator's smooth coefficient
dis_lambda=1 #Discriminator's lambda
dis_lr=learning_rate #Discriminator learing rate
encoder_lr=learning_rate #Encoder learing rate
RE_lr=learning_rate #Extractor learing rate
G_Times=5 #Number of times to train generator in one batch
D_Times=1 #Number of times to train discriminator in one batch
Orth_Coef=0.02 #orthogonality constraints coefficient
