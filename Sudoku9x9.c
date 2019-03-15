#include<stdio.h>
int check(int a[9][9],int size,int line,int pos,int num){
  int i,j,col,row;
  for(i=0;i<size;i++){
       if(a[line][i]==num && i!=pos)
         return 0;
       if(a[i][pos]==num && i!=line)
         return 0;
       }
  row=(line<3)?0:(line<6)?3:6;
  col=(pos<3)?0:(pos<6)?3:6;
 for(i=row;i<row+3;i++){
  for(j=col;j<col+3;j++){
      if(a[i][j]==num && (i!=line || j!=pos))
       return 0;
   }
  }
  return 1;
}

int sudoku(int s[9][9],int size,int line,int col,int num){
if(s[line][col]!=0){
if(line+1==size && col+1==size)
  return 1;
if((col+1)%size==0)
return sudoku(s,size,line+1,(col+1)%size,1);
else
return sudoku(s,size,line,(col+1)%size,1);
}
else{

while(num<10){
if(check(s,size,line,col,num)){
  s[line][col]=num;
  //printf("%d %d %d \n",line,col,num);
  if(line+1==size && col+1==size)
  return 1;

  if((col+1)%size==0){
    if(sudoku(s,size,line+1,(col+1)%size,1))
      return 1; 
    }
  else{ if(sudoku(s,size,line,(col+1)%size,1))
        return 1;
       }
   }
num=num+1;      
}
if(num==10){
 s[line][col]=0;
 return 0;
}
}
}
int main(){
int s[9][9];
int i,j,size=9;
char temp;
for(i=0;i<size;i++){
 for(j=0;j<size;j++){
  scanf("%c",&temp);
  s[i][j]=(int)temp-48; 
    }
  scanf("%c",&temp);
  }
if(sudoku(s,size,0,0,1)){
for(i=0;i<size;i++){
 for(j=0;j<size;j++)
  printf("%2d",s[i][j]);
printf("\n");
}
}
}
