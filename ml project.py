##classification of IRIS flower using machine learning
##load IRIS data to program
import tkinter.messagebox as m
from tkinter import *
w=Tk()
w.geometry("500x500")
from sklearn.datasets import load_iris
iris=load_iris()
print(iris)
######separate input and output
X=iris.data   ###numpy array  input
Y=iris.target  ##numpy array  output
print(X)
print(Y)
print(X.shape)  #(150,4) 150 rows 4 columns
print(Y.shape)  #(150,)
##########################
##split (randomly)dataset for a training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
##80% for training 20 %for testing
print(X_train.shape)#(120,4)
print(Y_train.shape)#(120,)
print(X_test.shape)#(30,4)
print(Y_test.shape)#(30,)
#####################################################################
def KNN():
    global acc_knn
    global K
    #KNN algorithm
    from sklearn.neighbors import KNeighborsClassifier
    K=KNeighborsClassifier(n_neighbors=5)
    K.fit(X_train,Y_train)
    Y_pred=K.predict(X_test)
    #Find accuracy
    from sklearn.metrics import accuracy_score
    acc_knn=accuracy_score(Y_test,Y_pred)
    acc_knn=round(acc_knn*100,2)
    print("accuracy score in KNN is ",acc_knn,"%")
    m.showinfo(title="KNN" , message="accuracy is "+str(acc_knn)+"%")
def LG():
    global acc_lg
    global L
    #LG algorithm
    from sklearn.linear_model import LogisticRegression
    #create the model
    L=LogisticRegression(solver='liblinear',multi_class='auto')#ignore warning message
    #Train the model
    L.fit(X_train,Y_train)
    #Test the model
    Y_pred=K.predict(X_test)
    #Find accuracy
    from sklearn.metrics import accuracy_score
    acc_lg=accuracy_score(Y_test,Y_pred)
    acc_lg=round(acc_lg*100,2)
    print("accuracy score in LG is ",acc_lg,"%")
    m.showinfo(title="LG" , message="accuracy is "+str(acc_lg)+"%")
def DT():
    global acc_dt
    global D
    #dt algorithm
    from sklearn.tree import DecisionTreeClassifier
    #create the model
    D=DecisionTreeClassifier()
    #Train the model
    D.fit(X_train,Y_train)
    Y_pred=K.predict(X_test)
    #Find accuracy
    from sklearn.metrics import accuracy_score
    acc_dt=accuracy_score(Y_test,Y_pred)
    acc_dt=round(acc_dt*100,2)
    print("accuracy score in dt is ",acc_dt,"%")
    m.showinfo(title="DT" , message="accuracy is "+str(acc_dt)+"%")
def NB():
    global acc_nb
    global N
    #dt algorithm
    from sklearn.naive_bayes import GaussianNB
    #create the model
    N=GaussianNB()
    #Train the model
    N.fit(X_train,Y_train)
    Y_pred=N.predict(X_test)
    #Find accuracy
    from sklearn.metrics import accuracy_score
    acc_nb=accuracy_score(Y_test,Y_pred)
    acc_nb=round(acc_nb*100,2)
    print("accuracy score in nb is ",acc_dt,"%")
    m.showinfo(title="NB" , message="accuracy is "+str(acc_nb)+"%")
def Compare():
    import matplotlib.pyplot as plt
    model=["KNN","LG","NB","DT"]
    accuracy=[acc_knn,acc_lg,acc_nb,acc_dt]
    plt.bar(model,accuracy,color=["orange","red","blue","green"])
    plt.xlabel("Models")
    plt.ylabel("Accuracy")
    plt.show()
def Submit():
    sl=float(v1.get())
    sw=float(v2.get())
    pl=float(v3.get())
    pw=float(v4.get())
    R=[acc_knn,acc_lg,acc_nb,acc_dt]
    ##P=max(R)
    if max(R)== acc_knn:
        result = K.predict([[sl,sw,pl,pw]])
        m.showinfo(title="accuracy test",message="KNN")
    elif max(R)==acc_lg:
        result = L.predict([[sl,sw,pl,pw]])
        m.showinfo(title="accuracy test",message="LG")
    elif max(R)==acc_dt:
        result=D.predict([[sl,sw,pl,pw]])
        m.showinfo(title="accuracy test",message="LG")
    else:
        result=N.predict([[sl,sw,pl,pw]])
        m.showinfo(title="accuracy test",message="NB")
    if result ==0:
        flower="setosa"
    elif result == 1:
        flower = "versicolor"
    elif result == 2:
        flower ="verginia"
    m.showinfo(title="IRIS flower 0",message = "flower "+flower)
def Reset():
    v1.set("")
    v2.set("")
    v3.set("")
    v4.set("")


########Design GUI##########
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()

e1=Entry(w,font=("arial",20,"bold"),textvariable=v1)
e2=Entry(w,font=("arial",20,"bold"),textvariable=v2)
e3=Entry(w,font=("arial",20,"bold"),textvariable=v3)
e4=Entry(w,font=("arial",20,"bold"),textvariable=v4)
l1=Label(w,text="Enter flower data",font=("arial",20,"bold"))
l2=Label(w,text="SL",font=("arial",20,"bold"))
l3=Label(w,text="SW",font=("arial",20,"bold"))
l4=Label(w,text="PL",font=("arial",20,"bold"))
l5=Label(w,text="PW",font=("arial",20,"bold"))
b1=Button(w,text="KNN",command=KNN,font=("arial",18,"bold"))
b2=Button(w,text="LG",command=LG,font=("arial",20,"bold"))
b3=Button(w,text="DT",command=DT,font=("arial",20,"bold"))
b4=Button(w,text="NB",command=NB,font=("arial",20,"bold"))
b5=Button(w,text="Compare",command=Compare,font=("arial",20,"bold"))
b6=Button(w,text="Submit",command=Submit,font=("arial",20,"bold"))
b7=Button(w,text="Reset",command=Reset,font=("arial",20,"bold"))
e1.grid(row=2,column=4,columnspan=5)
e2.grid(row=3,column=4,columnspan=5)
e3.grid(row=4,column=4,columnspan=5)
e4.grid(row=5,column=4,columnspan=5)
l1.grid(row=1,column=3,columnspan=4)
l2.grid(row=2,column=3)
l3.grid(row=3,column=3)
l4.grid(row=4,column=3)
l5.grid(row=5,column=3)
b1.grid(row=1,column=1)
b2.grid(row=2,column=1)
b3.grid(row=3,column=1)
b4.grid(row=4,column=1)
b5.grid(row=6,column=1)
b6.grid(row=6,column=5)
b7.grid(row=6,column=7)
w.mainloop()


