using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Leap;
using Leap.Unity;
public class Scene_leap : MonoBehaviour {

    // Use this for initialization
    LeapProvider provider;
    LineRenderer line;
    RaycastHit hit;

    bool open_ray = false;

    private const float rotate_sensitive = 1500f;  //旋转灵敏度
    private const float displacement_sensitive = 0.015f; //位移灵敏度
    private const float rotate_initial_value = 0f;  //旋转初始位置值
    const float smallestVelocity = 0.5f;
    const float deltaVelocity = 0.77f;//0.77f;
    const float deltaCloseFinger = 0.09f;

    
    public GameObject Back_Main;
    void Start () {
        line = GetComponent<LineRenderer>();
        provider = FindObjectOfType<LeapProvider>() as LeapProvider;
        line.SetVertexCount(2);
        
	}
	
	// Update is called once per frame
	void Update () {
        line.SetWidth(0.02f, 0.02f);
        line.SetColors(Color.yellow, Color.red);
        Frame frame = provider.CurrentFrame;
        foreach(var hand in frame.Hands)
        {
            //Debug.Log(hand.PinchDistance);
            if (hand.IsLeft)
            {
                if (hand.IsLeft)
                {
                    if (isMoveLeft(hand))
                    {
                        open_ray = false;
                    }
                    if (isMoveRight(hand))
                    {
                        open_ray = true;
                    }
                }
                if (open_ray)
                {
                    Debug.DrawRay(hand.WristPosition.ToVector3(), hand.Direction.ToVector3().normalized, Color.red);
                    Ray ray = new Ray(new Vector3(hand.WristPosition.ToVector3().x, hand.WristPosition.ToVector3().y + 0.04f, hand.WristPosition.ToVector3().z), hand.Direction.ToVector3().normalized);
                    bool rayCast = Physics.Raycast(ray, out hit, 500);
                    line.SetPosition(0, (new Vector3(hand.WristPosition.ToVector3().x, hand.WristPosition.ToVector3().y + 0.04f, hand.WristPosition.ToVector3().z)));
                    line.SetPosition(1, hand.Direction.ToVector3().normalized * 999999);
                    if (rayCast)
                    {
                        Debug.Log(hit.collider.name);
                       if (hit.collider.name == "")
                        {
                            line.SetPosition(1, hit.transform.position);
                            if (isCloseHand(hand))
                            {
                                this.gameObject.GetComponent<LineRenderer>().SetWidth(0.000000001f, 0.000000001f);
                                foreach (var v in )
                                {
                                   
                                }
                            }
                            if (isOpenFullHand(hand))
                            {
                                this.gameObject.GetComponent<LineRenderer>().SetWidth(0.02f, 0.02f);
                                foreach (var v in )
                                {
                                    v.GetComponent<UISprite>().enabled = false;
                                }
                            }
                        }
                        

                        
                    }
                }
                else
                {
                    this.gameObject.GetComponent<LineRenderer>().SetWidth(0.000000001f, 0.000000001f);
                }
            }
        }
		
	}

    protected bool isCloseHand(Hand hand)     //是否握拳 
    {
        List<Finger> listOfFingers = hand.Fingers;
        int count = 0;
        //bool is_closed = false;
        for (int f = 0; f < listOfFingers.Count; f++)
        { //循环遍历所有的手~~
            Finger finger = listOfFingers[f];
            if ((finger.TipPosition - hand.PalmPosition).Magnitude < deltaCloseFinger)    // Magnitude  向量的长度 。是(x*x+y*y+z*z)的平方根。    //float deltaCloseFinger = 0.05f;
            {
                count++;
                //is_closed = true;
                //  if (finger.Type == Finger.FingerType.TYPE_THUMB)
                //  Debug.Log ((finger.TipPosition - hand.PalmPosition).Magnitude);
            }
        }
        return (count == 5);
        // return hand.GrabStrength == 1;
        //return is_closed;
    }
    protected bool isCloseHande(Hand hand)     //是否握拳 
    {
        List<Finger> listOfFingers = hand.Fingers;
        int count = 0;
        //bool is_closed = false;
        for (int f = 0; f < listOfFingers.Count; f++)
        { //循环遍历所有的手~~
            Finger finger = listOfFingers[f];
            if ((finger.TipPosition - hand.PalmPosition).Magnitude < 1.5f)    // Magnitude  向量的长度 。是(x*x+y*y+z*z)的平方根。    //float deltaCloseFinger = 0.05f;
            {
                count++;
                //is_closed = true;
                //  if (finger.Type == Finger.FingerType.TYPE_THUMB)
                //  Debug.Log ((finger.TipPosition - hand.PalmPosition).Magnitude);
            }
        }
        return (count == 5);
        // return hand.GrabStrength == 1;
        //return is_closed;
    }

    protected bool isOpenFullHand(Hand hand)         //手掌全展开~
    {
        //Debug.Log(hand.GrabStrength + " " + hand.PalmVelocity + " " + hand.PalmVelocity.Magnitude);
        return hand.PinchStrength == 0;

    }
    protected bool isStationary(Hand hand)// 固定不动的 
    {
        return hand.PalmVelocity.Magnitude < smallestVelocity;
    }
    public bool isMoveUp(Hand hand)   //手向上 
    {
        return hand.PalmVelocity.y > 0.77f/*deltaVelocity*/ && !isStationary(hand);
    }
    //protected bool isMoveUpa(Hand hand)   //手向上 
    //{
    //    return hand.PalmVelocity.y > deltaVelocity+0.3f && !isStationary(hand);
    //}
    protected bool isMoveDown(Hand hand) //手向下  
    {
        return hand.PalmVelocity.y < -deltaVelocity && !isStationary(hand);
    }
    protected bool isMoveLeft(Hand hand)   // 手划向左边
    {
        //x轴移动的速度   deltaVelocity = 0.7f    isStationary (hand)  判断hand是否禁止 
        return hand.PalmVelocity.x < -deltaVelocity && !isStationary(hand);
    }
    protected bool isMoveRight(Hand hand)// 手划向右边
    {
        return hand.PalmVelocity.x > deltaVelocity && !isStationary(hand);
    }
    protected bool isPaishou(Hand handl, Hand handr)
    {
        //Debug.Log("Running!");
        return (handl.PalmPosition == handr.PalmPosition) && !isStationary(handl);
    }
    public bool isMoveForward(Hand hand)
    {
        return hand.PalmVelocity.z > deltaVelocity && !isStationary(hand);
    }
    public bool isMoveBack(Hand hand)
    {
        return hand.PalmVelocity.z < -deltaVelocity && !isStationary(hand);
    }
}
