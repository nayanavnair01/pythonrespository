����   A M  java1/evenorodd  java/lang/Object <init> ()V Code
  	   LineNumberTable LocalVariableTable this Ljava1/evenorodd; main ([Ljava/lang/String;)V  java/util/Scanner	    java/lang/System   in Ljava/io/InputStream;
     (Ljava/io/InputStream;)V	     out Ljava/io/PrintStream;   enter a number:
 " $ # java/io/PrintStream % & println (Ljava/lang/String;)V
  ( ) * nextInt ()I   , - . makeConcatWithConstants (I)Ljava/lang/String;  ,  , args [Ljava/lang/String; sc Ljava/util/Scanner; num I StackMapTable 
SourceFile evenorodd.java BootstrapMethods
 < > = $java/lang/invoke/StringConcatFactory - ? �(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/invoke/CallSite; ; B the number: D 
 is even  F  is odd InnerClasses I %java/lang/invoke/MethodHandles$Lookup K java/lang/invoke/MethodHandles Lookup !               /     *� �    
                    	       �     F� Y� � L� � !+� '=� � +  � !p� � � /  � !� � � 0  � !�    
   & 	          $ 	 * 
 6  9  E          F 1 2    ; 3 4   . 5 6  7   
 � 9   8    9 :     @  A @  C @  E G   
  H J L 