using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class MOV : MonoBehaviour,IDragHandler,IDropHandler //实现接口，显示调用
{
    private RectTransform rt; //RectTransform是UI的位置信息
    public RectTransform cavansRt;
    bool is_first = true;
    Vector2 paneUtility; //UI位置信息为Vector2
	
    public void OnDrag(PointerEventData eventData) //拖动中实现的
    {
        Vector2 MousePosition = eventData.position;
        Vector2 UguiPos = new Vector2();
        bool isBian = RectTransformUtility.ScreenPointToLocalPointInRectangle(cavansRt.transform as RectTransform, MousePosition, eventData.enterEventCamera, out UguiPos);
        if(is_first)
        {
            is_first = false;
            RectTransformUtility.ScreenPointToLocalPointInRectangle(rt, MousePosition, eventData.enterEventCamera, out paneUtility);
        }
        if(isBian)
        {
            rt.anchoredPosition = UguiPos-paneUtility;
        }
       // Debug.Log("Drag ME!");
    }

    // Start is called before the first frame update
    void Start() //初始化
    {
        rt = gameObject.transform as RectTransform;
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void OnDrop(PointerEventData eventData) //拖动完成后
    {
        Debug.Log("Drop");
        is_first = true; //结束这一次的拖动，再次设置为第一次
        //throw new System.NotImplementedException();
    }
}