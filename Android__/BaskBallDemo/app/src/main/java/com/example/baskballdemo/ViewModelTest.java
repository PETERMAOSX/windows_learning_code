package com.example.baskballdemo;

import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class ViewModelTest extends ViewModel {
    private MutableLiveData<Integer> A_teamValue;
    private MutableLiveData<Integer> B_teamValue;
    private int Ascore,Bscore;

    public MutableLiveData<Integer> getA_teamValue() {
        if(this.A_teamValue == null){
            this.A_teamValue = new MutableLiveData<>();
            this.A_teamValue.setValue(0);
        }
        return A_teamValue;
    }

    public MutableLiveData<Integer> getB_teamValue() {
        if(this.B_teamValue == null){
            this.B_teamValue = new MutableLiveData<>();
            this.B_teamValue.setValue(0);
        }
        return B_teamValue;
    }
    public void A_add(int n){
        this.Ascore = this.A_teamValue.getValue();
        this.Bscore = this.B_teamValue.getValue();
        this.A_teamValue.setValue(this.A_teamValue.getValue()+n);
    }
    public void B_add(int n){
        this.Ascore = this.A_teamValue.getValue();
        this.Bscore = this.B_teamValue.getValue();
        this.B_teamValue.setValue(this.B_teamValue.getValue()+n);
    }
    public void reset(){
        this.A_teamValue.setValue(0);
        this.B_teamValue.setValue(0);
    }
    public void undo(){
        this.A_teamValue.setValue(this.Ascore);
        this.B_teamValue.setValue(this.Bscore);

    }


}
