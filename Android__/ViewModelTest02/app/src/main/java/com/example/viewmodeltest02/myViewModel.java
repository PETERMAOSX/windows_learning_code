package com.example.viewmodeltest02;

import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class myViewModel extends ViewModel {
    public MutableLiveData<Integer> myitem;

    public MutableLiveData<Integer> getMyitem() {
        if(this.myitem == null){
            this.myitem = new MutableLiveData<>();
            myitem.setValue(0);
        }
        return myitem;
    }
    public void Add(){
        this.myitem.setValue(this.myitem.getValue()+1);
    }
}
