{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9e8dcc91",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\yash.hemnani\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n",
      "[nltk_data] Downloading package wordnet to\n",
      "[nltk_data]     C:\\Users\\yash.hemnani\\AppData\\Roaming\\nltk_data...\n"
     ]
    }
   ],
   "source": [
    "#Module to perform text pre processing and normalisation\n",
    "\n",
    "#Imports\n",
    "import nltk\n",
    "nltk.download(\"stopwords\")\n",
    "from nltk .corpus import stopwords\n",
    "\n",
    "import spacy\n",
    "from nltk.stem.porter import PorterStemmer\n",
    "\n",
    "from nltk.stem import WordNetLemmatizer\n",
    "nltk.download('wordnet')\n",
    "\n",
    "stop = stopwords.words('english')\n",
    "\n",
    "\n",
    "### Functions ###\n",
    "\n",
    "\n",
    "#Function to convert all uppercase text into lowercase\n",
    "\n",
    "def To_Lower(df, column_name):\n",
    "    df[column_name] = df[column_name].str.lower()\n",
    "    return df\n",
    "\n",
    "\n",
    "#Function to remove all HTML break tags\n",
    "def Remove_HTML_Tag(df, column_name):\n",
    "    df[column_name] = [doc.replace(\"<br />\", \" \") for doc in df.column_name]\n",
    "    return df\n",
    "\n",
    "\n",
    "#Function to remove all special characters from text\n",
    "\n",
    "def Remove_Special_Char(df, column_name):\n",
    "    df[column_name] = df[column_name].str.replace('[^$@#[`\\];:\\'\\\\]','')\n",
    "    return df\n",
    "\n",
    "#Function for removing the StopWords\n",
    "\n",
    "def Remove_Stopwords(df, column_name):\n",
    "    df[column_name] = df[column_name].apply(stopwords)\n",
    "    return df\n",
    "\n",
    "#Function to perform all pre-processing tasks\n",
    "def Perform_Preprocessing(df, column_name):\n",
    "    df = To_Lower(df, column_name)\n",
    "    df = Remove_HTML_Tag(df, column_name)\n",
    "    df = Remove_Special_Char(df, column_name)\n",
    "    df = Remove_Stopwords(df, column_name)\n",
    "    return df\n",
    "\n",
    "\n",
    "#Function to perform Stemming Normalisation\n",
    "\n",
    "def Perform_Stemming(Column_Elements):\n",
    "    stemmer = PorterStemmer()\n",
    "    return [' '.join([stemmer.stem(word) for word in element.split()]) for element in Column_Elements]\n",
    "\n",
    "\n",
    "def lemmatize_text(Column_Elements):\n",
    "    w_tokenizer = nltk.tokenize.WhitespaceTokenizer()\n",
    "    lemmatizer = WordNetLemmatizer()\n",
    "    text = [lemmatizer.lemmatize(word) for word in w_tokenizer.tokenize(review)]\n",
    "    return \" \".join(text)\n",
    "\n",
    "\n",
    "#Function to perform Lemmatization Normalization\n",
    "\n",
    "def Perform_Lemmatization(df, column_name):\n",
    "    df[column_name] = df[column_name].apply(lemmatize_text)\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7aae348b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
